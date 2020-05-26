
https://leetcode.com/discuss/interview-question/system-design/124603/how-to-handle-large-log-data-and-store-particular-info-to-sql/232689


STREAMING BASED SOLUTION: convert/capture each log statement a event. Stream these events to a streaming processing Framework. Kafka Streams/Apache S4/Storm etc and then store relevant data, ignore the rest.
OFFLINE/BATCH PROCESSING: Store files in a filesystem, use map-reduce or any big data/ETL technology to extract useful information

Instead of logging the info via logs (which makes things slow) we could also look to capture specific events by writing a JS that captures the data and send these events to a microservice (like we do for web-analytics) and the microservice saves it. [its a little bit off track but depending on what kind of data you want to track, this may be a viable option]

