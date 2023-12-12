/* 
* Shell scripts from GitHub sample repositories 
* Returns 15626 rows
*/
SELECT id, size, content, sample_repo_name, sample_path FROM `bigquery-public-data.github_repos.sample_contents` \
    WHERE sample_path LIKE '%.sh';

/* 
* Batch files from GitHub sample repositories 
* Returns 2204 rows
*/
SELECT id, size, content, sample_repo_name, sample_path FROM `bigquery-public-data.github_repos.sample_contents` \
    WHERE sample_path LIKE '%.bat';

/* 
* Dockerfile(s) from GitHub sample repositories 
* Returns 1413 rows
*/
SELECT id, size, content, sample_repo_name, sample_path FROM `bigquery-public-data.github_repos.sample_contents` \
    WHERE sample_path LIKE '%Dockerfile';
