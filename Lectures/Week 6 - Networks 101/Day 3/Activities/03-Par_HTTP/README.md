# Analyzing HTTP

In this activity, you'll peer into HTTP conversations and start to reverse-engineer HTTP protocol.

## Instructions

### Browsing BBC

- Open `bbc.pcapng`. This contains data captured while surfing for news and contains examples of several new status codes.

  - Refer to this [HTTP Status Code Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) as you go.

- The first packet in `example.pcapng` was a GET request for a resource. Filter for traffic to the BBC and find the same GET request.

- Follow the HTTP stream. Do the request/response for the resource look the same as they did for `www.example.com`? How are they different?

  - What's the status code on the response? What does this code mean?

- Look for the request for `/news/1.55.2536/img/news--icons-sprite.png`.

  - What's the status code on the response? What does this code mean?

  - What kind of server sent this response?

- Look for the request for `/track/cmf/generic?ttd_pid=icco6m5&ttd_tpi=1`.

  - What's the status code on the response? What does this code mean?

### POST Requests

- Open `http_post.pcapng`.

- Follow the HTTP stream of the fourth packet in the capture.

  - How is the first line of this request different from the GET requests you've seen so far?

  - How is the last line of this request different from the GET requests you've seen so far?

- Check out this [reference on HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

  - What does this kind of request do?

  - What are some ways it is different from a GET request?

### Wrapping Up

- Define the shape of an HTTP request/response.

  - What does the first line of an HTTP request/response look like? What does each piece represent?

  - What do the remaining lines of an HTTP request/response look like? What is the format for each of these lines?

  - Does anything change based on the request method? If so, what?
