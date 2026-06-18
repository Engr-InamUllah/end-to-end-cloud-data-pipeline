import sqlite3,tempfile,unittest
from pathlib import Path
from src.pipeline import run
class PipelineTest(unittest.TestCase):
 def test_loads_valid_rows(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/"x.csv").write_text("event_date,customer_id,amount\n2026-01-01,C1,12.5\n2026-01-02,,5\n")
   self.assertEqual(run(p/"x.csv",p/"db.sqlite"),1)
   with sqlite3.connect(p/"db.sqlite") as db:self.assertEqual(db.execute("select count(*) from sales").fetchone()[0],1)
if __name__=="__main__":unittest.main()