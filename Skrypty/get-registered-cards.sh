#!/bin/bash

sqlite3 "${DOOR_HOME}/doors.db" < "${DOOR_HOME}/Kod/SQL/4-get-registered-cards.sql"
