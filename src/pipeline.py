import csv, sqlite3
from pathlib import Path

def run(source: Path, database: Path) -> int:
    rows=list(csv.DictReader(source.open(encoding="utf-8")))
    clean=[(r["event_date"],r["customer_id"],float(r["amount"])) for r in rows if r["customer_id"] and float(r["amount"])>=0]
    database.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(database) as db:
        db.execute("create table if not exists sales(event_date text, customer_id text, amount real)")
        db.execute("delete from sales"); db.executemany("insert into sales values(?,?,?)",clean); db.commit()
    return len(clean)
if __name__=="__main__": run(Path("data/events.csv"),Path("output/warehouse.db"))