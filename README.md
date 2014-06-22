##ClearOS Tomcat Server Application

A ClearOS marketplace application for installing and administering the Apache Tomcat servlet and JSP container.

###Application Feature Goals

- Provide a ClearOS Marketplace application which installs Tomcat 7.x and other requirements onto a ClearOS system.
- The ClearOS application will allow user configurable environment settings for Tomcat's runtime.
- Allow authenticated access to the Apache Tomcat deployment manager, and host manager interfaces.

###ClearOS Integration Goals
- Integrate with ClearOS Webserver app to allow mod\_proxy and mod\_proxy\_ajp configurations for web app contexts.
- Integrate with ClearOS Firewall to allow Tomcat and Tomcat HTTPS services to be added.
- Integrate with ClearOS Certificate Management to allow manipulation of Java keystores for web apps.
- Integrate with ClearOS Flexshare to allow WAR deployment access.
