Issue Summary
Duration: August 14, 2024, 2:15 PM to August 14, 2024, 4:00 PM (EAT)
Impact: Our e-commerce platform's search functionality was completely unavailable for nearly two hours. This led to a significant drop in user engagement, with over 85% of users unable to search for products, and a noticeable decrease in sales during the outage. The root cause was traced back to an unexpected overload of the search service due to a surge in traffic that the system was not adequately prepared for.
Root Cause: The search service was overwhelmed by a sudden influx of requests, which was caused by a misconfiguration in the caching layer. The cache was not properly primed, leading to an excessive number of queries hitting the database directly.
Timeline
2:15 PM: Monitoring alert triggered, indicating a spike in database query times and a corresponding drop in successful searches.
2:20 PM: I started investigating the issue, initially suspecting a database performance problem. I assumed that a recent update to the database schema might be the culprit.
2:30 PM: After ruling out the database schema changes, I checked the search service logs and noticed a high number of incoming requests. I mistakenly thought it might be a DDoS attack due to the unusual traffic patterns.
2:45 PM: Escalated the issue to the infrastructure team. They quickly identified that the caching layer wasn’t functioning correctly. This discovery shifted our focus from the database to the cache.
3:00 PM: After a thorough review, we pinpointed a misconfiguration in the cache settings that prevented it from storing frequently accessed search results. This led to a flood of queries directly to the database.
3:15 PM: The cache configuration was corrected, and the cache was successfully primed with popular search queries. Traffic started to stabilize, and search functionality began to recover.
4:00 PM: The service was fully restored, and monitoring confirmed that search performance was back to normal. The incident was marked as resolved.
Root Cause and Resolution
Root Cause: The root of the problem was a misconfigured cache layer. The cache was not set up to store the most frequently accessed search results, leading to a dramatic increase in database queries. This overwhelmed the database, causing slow response times and, ultimately, the search service outage.
Resolution: The cache configuration was updated to ensure that popular search queries were stored correctly. We also performed a manual priming of the cache to ensure it was populated with the necessary data before bringing the service back online. This immediately reduced the load on the database, allowing the search service to resume normal operations.
Corrective and Preventative Measures
Improvements:
Revise the cache configuration process to prevent similar issues in the future.
Implement additional monitoring specifically for the caching layer to detect misconfigurations early.
Set up automated cache priming for high-traffic periods to avoid cache-related outages.
Tasks:
 Update documentation on cache configuration best practices.
 Enhance the monitoring system to include alerts for cache performance anomalies.
 Schedule training sessions for the team on advanced caching strategies.
 Develop and test automated cache priming scripts for deployment during peak traffic periods.
