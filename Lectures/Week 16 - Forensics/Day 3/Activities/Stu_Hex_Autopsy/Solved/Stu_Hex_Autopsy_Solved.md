### Review of Decoding Hex Data in Tracy's iPhone (0:10)

* Review the answers to the decoding exercise:

    1. `48 65 6c 6c 6f 20 57 6f 72 6c 64` = Hello World

    2. `54 65 73 74 69 6e 67 20 31 32 33 21` = Testing 123!
    
    3. `41 6e 64 72 65 77` =  Andrew

    4. `31 20 32 20 33 20 34 20 35 20 36` 1 2 3 4 5 6

Now, move onto the Browsing data dump.

* Call attention to the ASCII table in the far right of the solution file. Point out that you can see `http` and `https` in several places.

* Point out that `http` is `68 74 74 70` in hex. You can identify URLs by searching for this sequence in the hex dump.

* Point out that you can identify the following URLs in the hex dump:

  - https://plus.google.com/app/plus/mp/571/#~loop:view=activity&aid=z13sefxiuunsefxry04cjlhqczrgfh4b51k

  - https://plus.google.com/app/plus/oob/mp/571/?login=1

  - https://plus.google.com/app/plus/mp/571/?login=1

  - https://plus.google.com/app/plus/oob/mp/571/?login=1

  - https://accounts.google.com/ServiceLoginAuth

  - https://plus.google.com/app/plus/mp/571/?login=1

  - http://www.google.com/search?q=gorgonzola&ie=UTF-8&oe=UTF-8&hl=en&client=safari

* These URLs show that Tracy was browsing Google+. It's unclear from the browsing history alone, but the repeated visits to the `login` endpoint _may_ suggest  an attempt to break into an account (as opposed to a single successful login).

* The final URL indicates that Tracy searched for "Gorgonzola" on Google, using her Safari web browser.

* Point out that this browsing history could be used in the following ways:

  - Browsing history, along with timestamps, could provide an alibi for Tracy
  
  - Visiting peoples' Google+ profiles proves Tracy is in contact with them. This can be used as evidence that she knows someone she claims not to, or to prove a link to another party to the investigation— a common objective when building conspiracy cases.
  
  - Browsing history provides clues as to Tracy's interests. Searches related to the crime under investigation can be used as evidence against her. For instance, demonstrating that an individual accused of developing improvised explosives indeed downloaded handbooks on doing so is strong evidence against them.

- Summarize by emphasizing out that:

  - Hex is a lot easier to read then 1s and 0s
  - Reading hexdumps allows investigators to inspect non-ASCII evidence, such as memory dumps
  - Most digital forensics practitioners interrupt the hex code using charts, tools, or by sight. *It's okay for students to rely on automatic converters when dealing with hex and other encodings.*

- Answer any questions the students may have.
