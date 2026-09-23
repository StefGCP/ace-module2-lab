#!/usr/bin/env python3
import sys

path = 'routes/search.ts'
try:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    target = "models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)"
    repl = "models.sequelize.query('SELECT * FROM Products WHERE ((name LIKE :criteria OR description LIKE :criteria) AND deletedAt IS NULL) ORDER BY name', { replacements: { criteria: `%${criteria}%` } })"
    if target in c:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c.replace(target, repl))
        print("Successfully applied search.ts remediation patch.")
except Exception as e:
    print(f"Failed to apply patch: {e}")
