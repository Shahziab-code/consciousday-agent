from db.database import init_db, insert_entry, fetch_entries

def test_db():
    init_db()
    insert_entry("journal test", "intention", "dream", "priority1, priority2", "reflection", "strategy")
    entries = fetch_entries()
    assert len(entries) > 0
    print("DB test passed!")

if __name__ == "__main__":
    test_db()
