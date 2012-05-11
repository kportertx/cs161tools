#!/usr/bin/python

import os,sys,MySQLdb

# === DB operations related functions === #

def db_connect(dbname):

  try:  
    # Connect to the desired database.
    db_conn=MySQLdb.connect(host="localhost",user="root", passwd="madhacker",db=dbname)  
    cursor = db_conn.cursor()

    return cursor

  except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)


def select_load(cursor):
  # Should be expanded
  cur = cursor
  
  # Figure out the db table names
  sql = "SHOW TABLES;"
  cur.execute(sql)
  result = cur.fetchall()
  db_tables = []
  for entry in result:
    db_tables.append(entry[0])
  
  # Execute SELECT * queries against each table
  # and figure out the table with the most data
  table_size = {}
  for table_name in db_tables:
    sql = "SELECT * FROM " + table_name + ";"
    #printHeader(sql)
    cur.execute(sql)
    result = cur.fetchall()
    table_size[table_name] = len(result)
  
  # Figure out the columns associated with each
  # table so we can execute more simple queries
  table_columns = {}
  for table_name in db_tables:
    sql = "DESCRIBE " + table_name + ";"
    cur.execute(sql)
    #printHeader(sql)
    result = cur.fetchall()
    columns = []
    for entry in result:
      columns.append(entry[0] + ":" + entry[1])
    table_columns[table_name] = columns

  # === GROUP BY === SECTION ===

  # Find the most populated tables and execute 
  # some group by queries on them
  sql = "select distinct(city), meta_keywords from page group by city;"
  cur.execute(sql)
  #printHeader(sql)
  result = cur.fetchall()
  
  sql = "select distinct(contactCompany), contactName, contactEmail, contactBusPhone from leads group by contactCompany;"
  cur.execute(sql)
  #printHeader(sql)
  result = cur.fetchall()


  # Spread the workload across sales reps
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  for letter in alphabet: 
    sql = "select distinct(contactCompany) from leads where contactCompany like '" + letter + "%' and contactState like '%Not%' group by contactCompany LIMIT 100;" 
    cur.execute(sql)
    result = cur.fetchall()
    for entry in result:
      if not "'" in entry[0]:
        sql = "select contactCompany, contactName, contactEmail, contactBusPhone from leads where contactCompany = \'" + entry[0] + "\';"
        #printHeader(sql)

      else:
        param = (entry[0].replace("'", " ")).split(" ")
        sql = "select contactCompany, contactName, contactEmail, contactBusPhone from leads where contactCompany like \'%" + param[0] + "%\';"
        #printHeader(sql)
      cur.execute(sql)
      records = cur.fetchall()


  # === MORE Complex Queries ===
  sql = "select distinct(page_name), googleRank.searchTerm from page, googleRank where page.page_name = googleRank.page order by page_name;"
  #printHeader(sql)
  cur.execute(sql)
  result = cur.fetchall()
  location = result
  for entry in location:
    sql = "select position, searchTerm from page, googleRank where searchTerm like '%" + entry[1] + "%' group by searchTerm order by position asc;"
    #printHeader(sql) 
    cur.execute(sql)
    result = cur.fetchall()


def update_record(cursor, tablename):

  # Init variables.
  cur = cursor
  tbl = tablename
  manufacturer = ["Apple", "Brocade", "Canon", "Cisco", "Compaq", "Dell", "D-Link", "Emulex", "Extreme", "Force10", "Foundry", "HP", "Juniper", "Sillicon Mechanics", "Sonicwall", "Sony", "Sun"]

  # Populate manufacturer columns in the page table.
  sql = "select manufacturer, title from " + tbl + ";"
  cur.execute(sql)
  result = cur.fetchall()
  for entry in result:
    if not entry[0] or entry[0] == "empty":
      for maker in manufacturer:
        if maker in entry[1]:
          #printHeader("update page set manufacturer =\'" + maker + "\' where title = \'" + entry[1] + "\';")
          cur.execute("""update page set manufacturer=%s where title=%s""", (maker, entry[1]))
        else:
          continue
    else:
      continue
  
  # Now lets nuke what we did in order to setup the db for another run.
  for entry in result:
    if entry[0]:
      #printHeader("update page set manufacturer =\'empty\' where title = \'" + entry[1] + "\';")
      cur.execute("""update page set manufacturer=%s where title=%s""", ("empty", entry[1]))
    else:
      continue


def noiseLoad(cursor):
  cur = cursor
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
  for letter in alphabet:
    sql = "select distinct(word) from wordCounter where word like '" + letter + "%' order by word;" 
    cur.execute(sql)
    result = cur.fetchall()
    sql = "select count(*) from wordCounter where word like '" + letter + "%' order by word;"
    cur.execute(sql)
    result = cur.fetchall()
  
  sql = "select distinct(phrase), page from phraseCount group by page order by phrase;"
  cur.execute(sql)
  result = cur.fetchall()


def runQuery(cursor, query):
  cursor.execute(query)
  result = cursor.fetchall()

def printHeader(sql):
  header = "### Running query => " + sql + " ###"
  headerLen = len(header) - 1
  topHeader = '#'
  bottomHeader = '#'
  while headerLen > 0:
    topHeader += '#'
    bottomHeader += '#'
    headerLen -= 1
  #print topHeader
  #print header
  #print bottomHeader
  #print '"' + sql + '"'

  
# === Obviously we need a main function === #

if __name__ == '__main__':

  cursor = db_connect("npages")
  param = sys.argv[1]
  if param == "slt":
    select_load(cursor)
  elif param == "updt":
    update_record(cursor, "page")
  elif param == "random":
    noiseLoad(cursor)
  elif param == "full":
    select_load(cursor)
    update_record(cursor, "page")
    noiseLoad(cursor)
  else:
    runQuery(cursor, param)
