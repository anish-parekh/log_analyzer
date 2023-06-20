import os
import datetime
import random

log_directory = "/path/to/tomcat/logs"
process_name = "my_process"
num_log_files = 20
error_logs = [
    "SEVERE: Error processing request\njava.lang.NullPointerException\n    at com.example.MyServlet.doGet(MyServlet.java:25)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:741)\n    at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:231)\n    at ...",
    "SEVERE: Error deploying web application archive /path/to/war/app.war\njava.lang.ClassNotFoundException: com.example.MyClass\n    at org.apache.catalina.loader.WebappClassLoaderBase.loadClass(WebappClassLoaderBase.java:1364)\n    at org.apache.catalina.loader.WebappClassLoaderBase.loadClass(WebappClassLoaderBase.java:1186)\n    at org.apache.catalina.startup.WebappServiceLoader.loadServices(WebappServiceLoader.java:216)\n    at ...",
    "SEVERE: Servlet.service() for servlet [MyServlet] in context with path [/myapp] threw exception [java.lang.RuntimeException: Something went wrong] with root cause\njava.lang.RuntimeException: Something went wrong\n    at com.example.MyServlet.doGet(MyServlet.java:36)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:741)\n    at ...",
    "WARNING: Connection to database timed out after 10 seconds\norg.apache.tomcat.jdbc.pool.PoolExhaustedException: [pool-1-thread-1] Timeout: Pool empty. Unable to fetch a connection.\n    at org.apache.tomcat.jdbc.pool.ConnectionPool.borrowConnection(ConnectionPool.java:672)\n    at org.apache.tomcat.jdbc.pool.ConnectionPool.getConnection(ConnectionPool.java:200)\n    at org.apache.tomcat.jdbc.pool.DataSourceProxy.getConnection(DataSourceProxy.java:127)\n    at ...",
    "WARNING: Resource not found: /images/logo.png\njavax.servlet.ServletException: File [/images/logo.png] not found\n    at org.apache.catalina.servlets.DefaultServlet.serveResource(DefaultServlet.java:980)\n    at org.apache.catalina.servlets.DefaultServlet.doGet(DefaultServlet.java:461)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)\n    at ...",
    "SEVERE: Error executing SQL query\njava.sql.SQLException: Connection reset by peer\n    at com.example.MyDAO.executeQuery(MyDAO.java:78)\n    at com.example.MyService.processData(MyService.java:45)\n    at com.example.MyServlet.doGet(MyServlet.java:36)\n    at ...",
    "SEVERE: Error initializing application context\norg.springframework.beans.factory.BeanCreationException: Error creating bean with name 'myBean' defined in class path resource [applicationContext.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException\n    at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:563)\n    at ...",
    "WARNING: High CPU usage detected\ncom.example.monitoring.CPUMonitor: CPU usage above threshold\n    at com.example.monitoring.CPUMonitor.checkUsage(CPUMonitor.java:57)\n    at com.example.monitoring.MonitoringService.run(MonitoringService.java:98)\n    at ...",
    "SEVERE: Error parsing XML configuration file\norg.xml.sax.SAXParseException: The element type 'property' must be terminated by the matching end-tag '</property>'\n    at org.apache.xerces.parsers.DOMParser.parse(Unknown Source)\n    at org.apache.xerces.jaxp.DocumentBuilderImpl.parse(Unknown Source)\n    at ..."
]

# Create a directory for the process logs if it doesn't exist
process_logs_directory = os.path.join(log_directory, process_name)
if not os.path.exists(process_logs_directory):
    os.makedirs(process_logs_directory)

# Generate log files with real log messages and stop after an error occurs
for i in range(1, num_log_files+1):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(process_logs_directory, f"log_{timestamp}.txt")

    with open(log_file_path, "w") as log_file:
        # Write real log messages
        log_file.write(f"{datetime.datetime.now()} - INFO: Starting process {process_name}...\n")
        log_file.write(f"{datetime.datetime.now()} - INFO: Process {process_name} initialized.\n")
        log_file.write(f"{datetime.datetime.now()} - DEBUG: Processing data...\n")

        # Check if an error should occur
        should_error_occur = random.choice([True, False])
        if should_error_occur:
            error_log = random.choice(error_logs)
            log_file.write(f"{datetime.datetime.now()} - {error_log}\n")
            break  # Stop writing to the log file after an error occurs

    print(f"Log file {log_file_path} generated.")

print("Log files generation completed.")
