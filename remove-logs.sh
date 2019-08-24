#! /bin/bash

sqlite3 ${DOOR_HOME}/Kod/doors.db < ${DOOR_HOME}/Kod/SQL/3-remove-logs.sql
