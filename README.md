**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

./answer-img/default-namespace.png 

./answer-img/monitoring-namespace.png

./answer-img/observability-namespace.png

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

./answer-img/grafana-homepage.png


## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

./answer-img/grafana-prometheus.png


## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLO
- The application will have request response time 50ms during next month
- Our application will have an uptime of 95% during the next year


SLI
- The average time our application return a request during last month was 120ms
- Our application has 70% of uptime last year


## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

1. measuring count of http error
2. measuring pod cpu usage
3. measuring pod memory usage
4. measuring pod health / pod running status
5. measuring request/response time


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

include 4xx, 5xx Backend-Front end

./answer-img/grafana-metrics.png


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

./answer-img/jaeger-trace.png

./answer-img/jaeger-trace-2.png


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

./answer-img/Jaeger Dashboard.png


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:

./answer-img/error-ticket.docx

## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

1. measuring count of http error
2. measuring pod cpu usage
3. measuring pod memory usage
4. measuring pod health / pod running status


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. **Latency**
Showing the metrics of the time taken to serve a response from the request.
We want to show this to keep track of speed of our application and we want to make it faster

2. **Traffic**
Showing how much the average request time on the system
We want to show this to keep track of average request in our system, so we know the load of our apps just incase everything went wrong

3. **Saturation**
Showing Memory Usage, CPU Usage, keep track of our application resources usage, to make sure everything is fineC


## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

./answer-img/kpi-dashboard.png
