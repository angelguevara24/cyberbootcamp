# Resource Loading in Action

## Instructions

- Open Chrome, and open the Developer Tools with `Ctrl + Shift + I`.

- Navigate to `https://amazon.com`.

- Give the page a moment to load. When it's usable, look at the bottom of the Network inspector to see how many requests were fired.
  - What happens to this number when you scroll down on the page?
  - Where do you think the new requests are coming from?

- Inspect the resources in the list of requests. Find one requested from the domain `amazon.com`, and click on it.

- In the details pane on the right, click the **Headers** tab to see the request/response headers.
  - Which CORS headers should you look for in this request?

- Next, find a request for a resource from a different domain, and click on it.
  - Which CORS headers should you look for in this request?

- If you found CORS headers in either response above, record which headers you found; which values they had; and what they're for.
