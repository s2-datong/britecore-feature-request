## Approach
My primary approach to this project was building for scalability.
I used flask-restful to build the APIs due to the simple Resource abstraction it provides.
This way, additional features/endpoints can easily be implemented as Resources and mounted on the Flask App.

On the frontend I used plain javascript with bootstrap to build a simple UI. Ideally, a frontend framework such as Vue.js should be used. However, ES6 has become a pretty powerful language and a decent maintainable application can easily be built by taking advantage of the latest features in modern browsers.

I therefore opted not to use a frontend framework for this task.

The application starts with a login screen based on the asssumption that a staff would be entering these feature requests on behalf of clients. Such a staff should login to the system, in order for their activities to be tracked.