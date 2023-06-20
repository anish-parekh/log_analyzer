import os
import datetime
import random

log_directory = "/path/to/tomcat/logs"
process_name = "my_process"
num_log_files = 20
error_logs = [
    "ERROR: Error processing request\njava.lang.NullPointerException\n    at com.example.MyServlet.doGet(MyServlet.java:25)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:741)\n    at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:231)",
    "ERROR: Error deploying web application archive /path/to/war/app.war\njava.lang.ClassNotFoundException: com.example.MyClass\n    at org.apache.catalina.loader.WebappClassLoaderBase.loadClass(WebappClassLoaderBase.java:1364)\n    at org.apache.catalina.loader.WebappClassLoaderBase.loadClass(WebappClassLoaderBase.java:1186)\n    at org.apache.catalina.startup.WebappServiceLoader.loadServices(WebappServiceLoader.java:216)",
    "ERROR: Servlet.service() for servlet [MyServlet] in context with path [/myapp] threw exception [java.lang.RuntimeException: Something went wrong] with root cause\njava.lang.RuntimeException: Something went wrong\n    at com.example.MyServlet.doGet(MyServlet.java:36)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:741)",
    "ERROR: Connection to database timed out after 10 seconds\norg.apache.tomcat.jdbc.pool.PoolExhaustedException: [pool-1-thread-1] Timeout: Pool empty. Unable to fetch a connection.\n    at org.apache.tomcat.jdbc.pool.ConnectionPool.borrowConnection(ConnectionPool.java:672)\n    at org.apache.tomcat.jdbc.pool.ConnectionPool.getConnection(ConnectionPool.java:200)\n    at org.apache.tomcat.jdbc.pool.DataSourceProxy.getConnection(DataSourceProxy.java:127)",
    "ERROR: Resource not found: /images/logo.png\njavax.servlet.ServletException: File [/images/logo.png] not found\n    at org.apache.catalina.servlets.DefaultServlet.serveResource(DefaultServlet.java:980)\n    at org.apache.catalina.servlets.DefaultServlet.doGet(DefaultServlet.java:461)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)",
    "ERROR: Error executing SQL query\njava.sql.SQLException: Connection reset by peer\n    at com.example.MyDAO.executeQuery(MyDAO.java:78)\n    at com.example.MyService.processData(MyService.java:45)\n    at com.example.MyServlet.doGet(MyServlet.java:36)",
    "ERROR: Error initializing application context\norg.springframework.beans.factory.BeanCreationException: Error creating bean with name 'myBean' defined in class path resource [applicationContext.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException\n    at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:563)",
    "ERROR: High CPU usage detected\ncom.example.monitoring.CPUMonitor: CPU usage above threshold\n    at com.example.monitoring.CPUMonitor.checkUsage(CPUMonitor.java:57)\n    at com.example.monitoring.MonitoringService.run(MonitoringService.java:98)",
    "ERROR: Error parsing XML configuration file\norg.xml.sax.SAXParseException: The element type 'property' must be terminated by the matching end-tag '</property>'\n    at org.apache.xerces.parsers.DOMParser.parse(Unknown Source)\n    at org.apache.xerces.jaxp.DocumentBuilderImpl.parse(Unknown Source)",
    "ERROR: Failed to connect to database\njava.sql.SQLException: Connection refused\n    at com.example.DatabaseConnection.connect(DatabaseConnection.java:25)\n    at com.example.Application.start(Application.java:37)\n    at com.example.Application.main(Application.java:15)",
    "ERROR: Disk space running low\njava.io.IOException: No space left on device\n    at com.example.FileManager.writeToFile(FileManager.java:82)\n    at com.example.Application.processData(Application.java:58)\n    at com.example.Application.run(Application.java:32)",
    "ERROR: Failed to start service\norg.apache.commons.daemon.DaemonInitException: Failed to initialize service\n    at com.example.ServiceLauncher.init(ServiceLauncher.java:47)\n    at org.apache.commons.daemon.support.DaemonLoader.load(DaemonLoader.java:251)\n    at org.apache.commons.daemon.support.DaemonLoader.load(DaemonLoader.java:83)",
    "ERROR: Error processing request\njava.lang.IllegalArgumentException: Invalid input data\n    at com.example.RequestProcessor.process(RequestProcessor.java:55)\n    at com.example.RequestHandler.handleRequest(RequestHandler.java:78)\n    at com.example.Application.main(Application.java:24)",
    "ERROR: Failed to authenticate user\ncom.example.AuthenticationException: Invalid credentials\n    at com.example.UserAuthenticator.authenticate(UserAuthenticator.java:42)\n    at com.example.RequestHandler.processRequest(RequestHandler.java:92)\n    at com.example.Application.run(Application.java:32)",
    "ERROR: External service timeout\njava.net.SocketTimeoutException: Read timed out\n    at com.example.ServiceClient.sendRequest(ServiceClient.java:128)\n    at com.example.Application.processData(Application.java:58)\n    at com.example.Application.run(Application.java:32)",
    "ERROR: Database query failed\norg.hibernate.exception.SQLGrammarException: Invalid SQL syntax\n    at org.hibernate.exception.internal.SQLStateConversionDelegate.convert(SQLStateConversionDelegate.java:106)\n    at org.hibernate.exception.internal.StandardSQLExceptionConverter.convert(StandardSQLExceptionConverter.java:42)\n    at org.hibernate.engine.jdbc.spi.SqlExceptionHelper.convert(SqlExceptionHelper.java:113)",
    "ERROR: Error loading configuration\ncom.example.ConfigurationException: Missing required property\n    at com.example.ConfigurationLoader.load(ConfigurationLoader.java:67)\n    at com.example.Application.start(Application.java:37)\n    at com.example.Application.main(Application.java:15)",
    "ERROR: Failed to send email\njavax.mail.MessagingException: Could not connect to SMTP host\n    at javax.mail.Transport.send(Transport.java:157)\n    at com.example.EmailSender.send(EmailSender.java:48)\n    at com.example.Application.processData(Application.java:58)\n    at com.example.Application.run(Application.java:32)",
    "ERROR: Error executing batch job\norg.quartz.JobExecutionException: Job failed to execute\n    at org.quartz.core.JobRunShell.run(JobRunShell.java:227)\n    at org.quartz.simpl.SimpleThreadPool$WorkerThread.run(SimpleThreadPool.java:583)"
]

normal_logs = [
    "INFO: Application started",
    "DEBUG: Database connection established",
    "WARNING: Disk space running low",
    "INFO: User logged in",
    "DEBUG: API request received",
    "INFO: Task completed successfully",
    "DEBUG: Cache invalidated",
    "INFO: Configuration loaded",
    "DEBUG: Service started",
    "INFO: Resource accessed",
    "DEBUG: Request processing started",
    "WARNING: Network connection unstable",
    "INFO: Server restarted",
    "DEBUG: User session created",
    "INFO: Log file rotated",
    "DEBUG: Data transformation in progress",
    "WARNING: System performance degraded",
    "INFO: Email sent",
    "DEBUG: External service response received",
    "INFO: Task scheduled",
    "DEBUG: Request validation passed",
    "INFO: Operation completed",
    "DEBUG: Data synchronization started",
    "INFO: User profile updated",
    "DEBUG: API response sent",
    "WARNING: Missing configuration parameter",
    "INFO: Backup created",
    "DEBUG: File uploaded",
    "INFO: Resource deleted",
    "DEBUG: Request rate limited",
    "INFO: Server running in production mode",
    "DEBUG: Data encryption in progress",
    "INFO: Task aborted",
    "DEBUG: External dependency loaded",
    "INFO: Resource not found",
    "DEBUG: Request forwarded to backend",
    "WARNING: Unhandled exception caught",
    "INFO: Task initiated",
    "DEBUG: External dependency initialized",
    "INFO: Cache refreshed",
    "DEBUG: Data compression started",
    "INFO: Shutdown initiated",
    "DEBUG: Response formatting in progress",
    "INFO: User registered",
    "DEBUG: Database backup in progress",
    "INFO: Health check passed",
    "DEBUG: File downloaded",
    "INFO: System update available",
    "DEBUG: External dependency unavailable",
    "INFO: Task started",
    "DEBUG: Request throttled",
    "INFO: Service stopped",
    "DEBUG: Data validation in progress",
    "INFO: Resource not modified",
    "DEBUG: Request handling completed",
    "INFO: Configuration updated",
    "DEBUG: API rate limit exceeded"
]


# Create a directory for the process logs if it doesn't exist
process_logs_directory = os.path.join(log_directory, process_name)
if not os.path.exists(process_logs_directory):
    os.makedirs(process_logs_directory)

# Generate log files with real log messages and stop after an error occurs
for i in range(1, num_log_files + 1):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(process_logs_directory, f"log_{timestamp}.txt")

    with open(log_file_path, "w") as log_file:
        # Write real log messages
        log_file.write(f"{datetime.datetime.now()} - INFO: Starting process {process_name}...\n")
        log_file.write(f"{datetime.datetime.now()} - INFO: Process {process_name} initialized.\n")
        log_file.write(f"{datetime.datetime.now()} - DEBUG: Processing data...\n")

        # Generate a random number of log entries before the error log
        num_entries_before_error = random.randint(10, 50)
        for _ in range(num_entries_before_error):
            log_entry = random.choice(normal_logs)
            log_file.write(f"{datetime.datetime.now()} - {log_entry}\n")

        # Check if an error should occur
        should_error_occur = random.choice([True, False])
        if should_error_occur:
            error_log = random.choice(error_logs)
            log_file.write(f"{datetime.datetime.now()} - {error_log}\n")
            break  # Stop writing to the log file after an error occurs

    print(f"Log file {log_file_path} generated.")

print("Log files generation completed.")
