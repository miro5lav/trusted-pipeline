# GitHub → DuckDB example (Local Prefect Server)

Start Prefect Server
1. prefect server start

2. Register and run via Prefect Server
Register the flow with the server:
   uv run .\deploy_locally.py 
Then trigger it with 
   prefect deployment run 'main/my-deployment' 

3. Test and see data with get_github_data.py

Notes
- The DuckDB file (github_repos_issues.duckdb) will be created in the working directory.
