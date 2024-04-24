from datetime import date
from dataclasses import dataclass

@dataclass
class Posting:
    employer: str
    job: str
    url: str
    date_posted: date
    expiry_date: date