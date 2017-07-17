#To order by descending, or highest to lowest use desc()
from sqlalchemy import desc
stmt = select([tablename.columns.columnname])
rev_stmt = stmt.order_by(desc(tablename.columns.columnname))
rev_results = connection.execute(rev_stmt).fetchall()
print(rev_results[:10])
