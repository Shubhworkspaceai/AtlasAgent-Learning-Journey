from interaction_checker import load_interaction_db, find_interaction, DB_PATH

def test_db_load_and_lookup():
    db = load_interaction_db(DB_PATH)
    # a known high-risk lookup (order swapped on purpose)
    r = find_interaction("Aspirin", "Warfarin", db)
    assert r['level'].lower() == 'high' or r['level'].lower() == 'moderate'  # warfarin+aspirin is high in our DB
    # a known none
    r2 = find_interaction("Ibuprofen", "Metformin", db)
    assert r2['level'].lower() == 'none'
