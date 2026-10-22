Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Zootopia: Zootopia is a 2016 American 3D computer-animated comedy-adventure film produced by Walt Disney Animation Studios and released by Walt Disney Pictures.  It is the 55th Disney animated feature film.  The film was directed by Byron Howard and Rich Moore, co-directed by Jared Bush, and stars the voices of Ginnifer Goodwin, Jason Bateman, Idris Elba, Jenny Slate, Nate Torrence, Bonnie Hunt, Don Lake, Tommy Chong, J. K. Simmons, Octavia Spencer, Alan Tudyk, and Shakira.  The film details the unlikely partnership between a rabbit police officer and a red fox con artist as they uncover a conspiracy involving the disappearance of savage predator inhabitants of a mammalian metropolis.

Octavia Spencer: Octavia Lenora Spencer (born May 25, 1972) is an American actress and author.  She made her film debut in the 1996 drama film "A Time to Kill".  Her breakthrough came in 2011, when she starred as Minny Jackson in the period drama film "The Help", for which she won the Academy Award, Golden Globe, SAG, BAFTA, and Critics' Choice Movie Award for Best Supporting Actress.  She had a critically acclaimed performance in Ryan Coogler's drama "Fruitvale Station" (2013), for which she received the National Board of Review Award for Best Supporting Actress.  Spencer has received acclaim for her work in the films "Smashed" (2012), "Snowpiercer" (2013), "Get on Up" (2014), "The Divergent Series" (2015-2016), "Zootopia" (2016) and "The Shape of Water" (2017).  In 2017, she received Academy Award, Golden Globe, and SAG nominations for Best Supporting Actress for her performance as mathematician Dorothy Vaughan in the drama "Hidden Figures".

Ralph Breaks the Internet: Wreck-It Ralph 2: Ralph Breaks the Internet: Wreck-It Ralph 2 is an upcoming American 3D computer-animated comedy-adventure film that is being produced by Walt Disney Animation Studios.  It will be the sequel to 2012's "Wreck-It Ralph", and is scheduled to be released on November 21, 2018 by Walt Disney Pictures.

List of accolades received by Zootopia: "Zootopia" (known as "Zootropolis" in some territories) is a 2016 American 3D computer-animated buddy comedy film produced by Walt Disney Animation Studios and released by Walt Disney Pictures.  The film was directed by Byron Howard and Rich Moore and was based on a screenplay written by Jared Bush (who also co-directed) and Phil Johnston.  "Zootopia" focuses on the unlikely partnership between an ambitious rabbit police officer, Judy Hopps (voiced by Ginnifer Goodwin) and a crafty red fox con artist, Nick Wilde (voiced by Jason Bateman) as they uncover a conspiracy behind the mysterious disappearance of predators from a mammalian metropolis.

Up (2009 film): Up is a 2009 American 3D computer-animated comedy-adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.  Directed by Pete Docter, the film centers on an elderly widower named Carl Fredricksen (Ed Asner) and an earnest young "Wilderness Explorer" (a fictional youth group similar to the Boy Scouts) named Russell (Jordan Nagai).  By tying thousands of balloons to his home, Carl sets out to fulfill his dream to see the wilds of South America and complete a promise made to his late wife, Ellie.  The film was co-directed by Bob Peterson, with music composed by Michael Giacchino.

Meet the Robinsons: Meet the Robinsons is a 2007 American computer-animated science fiction comedy film produced by Walt Disney Animation Studios and released by Walt Disney Pictures on March 30, 2007.  The 47th Disney animated feature film, it was released in standard and Disney Digital 3-D versions.  The film is loosely based on characters from the children's book "A Day with Wilbur Robinson", by William Joyce.  The voice cast includes Jordan Fry, Wesley Singerman, Harland Williams, Tom Kenny, Steve Anderson, Laurie Metcalf, Adam West, Tom Selleck, and Angela Bassett.  It was the first film released after John Lasseter became chief creative officer of Walt Disney Animation Studios.

Cars (film): Cars is a 2006 American computer-animated comedy-adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.  Directed and co-written by John Lasseter, it is Pixar's final independently-produced motion picture before its purchase by Disney in May 2006.  Set in a world populated entirely by anthropomorphic cars and other vehicles, the film stars the voices of Owen Wilson, Paul Newman (in his final acting role), Bonnie Hunt, Larry the Cable Guy, Tony Shalhoub, Cheech Marin, Michael Wallis, George Carlin, Paul Dooley, Jenifer Lewis, Guido Quaroni, Michael Keaton, Katherine Helmond and John Ratzenberger.  Race car drivers Dale Earnhardt, Jr., Mario Andretti, Michael Schumacher and car enthusiast Jay Leno (as "Jay Limo") voice themselves.

Walt Disney Pictures: Walt Disney Pictures, Inc. is an American film production company and a subsidiary of Walt Disney Studios, owned by The Walt Disney Company.  The division is based at the Walt Disney Studios in Burbank, California, and is the main producer of live-action feature films within the Walt Disney Studios unit.  It took on its current name in 1983.  Today, in conjunction with the other units of Walt Disney Studios, Walt Disney Pictures is classified as one of Hollywood's "Big Six" film studios.  Films produced by Walt Disney Animation Studios and Pixar Animation Studios are also released under this brand.

Winnie the Pooh (2011 film): Winnie the Pooh is a 2011 American animated buddy musical comedy film produced by Walt Disney Animation Studios and released by Walt Disney Pictures.  It is the 51st Disney animated feature film.  Inspired by A. A. Milne's stories of the same name, the film is part of Disney's "Winnie the Pooh" franchise, the fifth theatrical "Winnie the Pooh" film released, and Walt Disney Animation Studios' second adaptation of "Winnie-the-Pooh" stories.  Jim Cummings reprises his vocal roles as Winnie the Pooh and Tigger, while series newcomers Travis Oates, Tom Kenny, Craig Ferguson, Bud Luckey, and Kristen Anderson-Lopez provide the voices of Piglet, Rabbit, Owl, Eeyore, and Kanga, respectively.  In the film, the aforementioned residents of the Hundred Acre Wood embark on a quest to save Christopher Robin from an imaginary culprit while Pooh deals with a hunger for honey.  The film is directed by Stephen Anderson and Don Hall, adapted from Milne's books by a story team led by Burny Mattinson, produced by Peter Del Vecho, Clark Spencer, John Lasseter, and Craig Sost, and narrated by John Cleese.

Walt Disney Studios Motion Pictures: Walt Disney Studios Motion Pictures (formerly Buena Vista Pictures Distribution and Buena Vista Film Distribution Company) is an American film distributor owned by The Walt Disney Company.  Established in 1953 as Buena Vista Film Distribution Company, the company handles theatrical distribution, marketing and promotion for films produced and released by the Walt Disney Studios, including Walt Disney Pictures, Walt Disney Animation Studios, Pixar Animation Studios, DisneyToon Studios, Marvel Studios, Lucasfilm, Disneynature, and Touchstone Pictures.  The division took on its current name in late 2007, which before that had been Buena Vista Pictures Distribution since 1987.

Question: Octavia Lenora Spencer, is an American actress and author, Spencer has received acclaim for her work in Zootopia, released in which year, an American 3D computer-animated comedy-adventure film produced by Walt Disney Animation Studios and released by Walt Disney Pictures?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "genre": {
          "type": "string",
          "description": "The primary genre of the film."
        },
        "animation_type": {
          "type": "string",
          "description": "The type of animation used for the film."
        },
        "production_studio": {
          "type": "string",
          "description": "The studio that produced the film."
        },
        "release_company": {
          "type": "string",
          "description": "The company that released the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre",
        "animation_type",
        "production_studio",
        "release_company"
      ],
      "additionalProperties": false
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress."
        },
        "received_acclaim_for_role": {
          "type": "boolean",
          "description": "Indicates if the actress received acclaim for her work in this specific film."
        }
      },
      "required": [
        "name",
        "received_acclaim_for_role"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "integer",
      "description": "The specific answer to the question, which is the release year of the film."
    }
  },
  "required": [
    "film_details",
    "actress_details",
    "question_answer"
  ],
  "additionalProperties": false
}
