# POC Dagster

## Step Dagster project

- Init project ``uvx create-dagster@latest project dagster-tutorial``
- Change to project dir ``cd dagster-tutorial``
- Activate env : ``source .venv/bin/activate``
- Install deps: ??
- Launch dg dev: ``dg dev``

## Add asset

- ``dg scaffold defs dagster.asset asset_file.py``
- Assets are associated to Definition
- Check if definitions are load correctly: ``dg check defs``
- Materialize assert: ``dg launch --assets asset_name1, asset_name2`` or ``"*"`` for all assets

## Resource

- Install respurce dep: ``uv add dagster-duckdb``
- Add resource file: ``dg scaffold defs dagster.resources resources.py``

## Dependencies

- They are defined by using the key ``dep```in the asset decorator

## Asset Check

- Check is the output of given asset meet are valid

## Automation

- Support scheduled and event-driven pipeline
- Create automation: ``dg scaffold defs dagster.schedule schedules.py``