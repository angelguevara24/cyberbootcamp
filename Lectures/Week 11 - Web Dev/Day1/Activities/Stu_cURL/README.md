# Getting Started with cURL

## Instructions

Navigate to the Postman Echo home page at: <https://docs.postman-echo.com/>

Use the documentation and examples to formulate the requests below. Note that all your requests will go to an endpoint at `https://postman-echo.com`, such as: `https://postman-echo.com/put`, etc.

- Send a GET request to the `/get` endpoint. Set the following query parameters:
  - `name`, with value equal to your name
  - `location` with value set to your current city
  - Record the URL you send your request to.
  - Be sure to wrap your URL in quotation marks!

- Find your query parameters in the beginning of the response data to verify they were sent properly.

- Next, resend the request above, but use the option to print out both request/response headers.

- The output from cURL has three sections:
  - A section at the top, with lines starting with `*`
  - The request in the middle, with lines starting with `>`
  - The response at the end, with lines starting with `<`

- Look at the section at the top.
  - What do you see in the first line that starts with `*`? What does this line indicate cURL is attempting to do?
  - Look at the line starting with `CAfile`. What do you think this file is for?
  - Look at the lines below, which start with `TLSv1.2`. Which protocol do these lines relate to? What do they imply for the rest of your communications for the server?

- Skip down to the request.
  - Identify your query parameters in the request line.
  - What is the value of the `User-Agent` header?
  - What kind of data does the client expect?

- Skip down to the response.
  - What is the status code of the response?
  - According to the headers, which kind of data does the response contain?
  - What kind of server is providing the response?
  - Identify your query parameters in the response.

- Next, send a POST request to the `/post` endpoint. Send the same data you sent as query parameters, but use cURL's `--data` option instead. 
  - Be sure to use the verbose flag to print out requests/responses.

- Look at the request.
  - Which headers are present in this request that you did not see in the GET request? Why were they added?
  - Identify where the data you sent appears in the request.

- Look at the end of the response data to verify that the server received your data, even if it isn't explicitly visible in the request.

## Questions

- Use the Postman Echo documentation to define the use cases for each of the below HTTP verbs.
  - GET
  - POST
  - OPTIONS
  - PUT
  - PATCH
  - DELETE