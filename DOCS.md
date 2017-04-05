#Technical Documentation

## Initial design

The **front end** will be implemented with simple HTML, CSS and jQuery. The aim is to keep the client side code light and with minimal design as outlined in the spec.
 
The web application **back end** will be implemented with python. Technical requirements are given in `GET_STARTED.md`. The application is run on the Flask framework for lightweight / fast development.

## Approach

Plan to build out a working front end and then, once the API has been mocked out, implement the back end to support the required search function.

The aim was to keep the code 'clean' and limit the amount of comments in the code. "Release notes" can be found in the github commit comments.

**KEEP IT SIMPLE** -- Developed witht he mindset of "iterative improvement" and "simple as possible". This means no extensive code infrastructure, class structure, etc.

Testing was targeted at the "functional" elements of the backend - namely the search. In a larger application I'd expect more extensive tests.

## Further improvements

Below are a list of next steps / features that could be added to improve the application. The improvements are split into sections.

### Front-end

**File Structure** -- Currently the front end is wrapped into a single file. This was to make development easier/quicker. It would be better to split out the javascript and css and minify them both.
 
**CSS** -- Rewrite in LESS/SASS depending on application type. Also use a UI kit like Bootstrap or Material.

**Application** -- Replace the raw .js with a simple single page application, probably Angular (or React).

**Mock** -- Clear out the mock. Left in for illustration.

### Back-end

**Database** -- The data format is relatively simple: JSON. With larger sets it would be more effective/efficient to store these in a database with faster search query.

**Search** -- This module was written to be very simple. It'd be better wrapped in a class and with the mock data in a second "mock class" so that these two implementations can be interchanged.

**Search: multiple key words** -- Split out the query string to include searching for multiple key words (separated by a space).

**Search: complex queries** -- Add in search specific query format (like Google) to allow searching on particular fields and forcing elements like case sensitivity.

**Search: ranking** -- Sort the results based on similarity to the query (search score).

**Search: api** -- The application has a basic api with query string. Move this to a more restful structure, allowing access to specific records using unique ids, etc.

**Architecture** -- If the search component became significantly more complex and that end point is hit more frequently than the route site, consider extracting the search into a separate API served service.

**Users** -- Add user or session based searching, returning results based on previous searches and adding in "recent searches" features.
 
**Security** -- The application has no security. Add in query parameter sanitisation.

### Analytics, Monitoring, Alerting

The application does't have any user anaylitics, event monitoring (i.e., can't access the database), generic server monitoring or support metric based alerting. In production, I would expect to see these.

### CI/CD
- deployment pipelines (Github -> Heroku?)
- automated testing (in the pipeline) + test environment
- merge request tests & environments (possible in Heroku)

### Features

The application has one feature: search. Depending on the use case, it may be desireable to add in user management, updating records, adding records, exporting data, etc.
