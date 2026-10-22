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
Alice in Wonderland (1999 film): Alice in Wonderland is a 1999 made-for-television film adaptation of Lewis Carroll's books "Alice's Adventures in Wonderland" and "Through the Looking-Glass".  It was first broadcast on NBC and then shown on British television on Channel 4.

La Ville dont le prince est un enfant (film): La Ville dont le prince est un enfant is a 1997 made-for-television film adapted from 1955 play by French dramatist Henry de Montherlant of the same title.

Bonanza: The Return: Bonanza: The Return is a 1993 made-for-television film sequel to both the 1959–1973 television series "Bonanza" and the 1988 made-for-television film "".  The movie was directed by Jerry Jameson and featured noted character actors Ben Johnson, Jack Elam, Dean Stockwell, Linda Gray, and Richard Roundtree.

Alice in Wonderland (1985 film): Alice in Wonderland is a 1985 two-part made-for-television film adaptation of Lewis Carroll's books "Alice's Adventures in Wonderland" and "Through the Looking-Glass".  An Irwin Allen production, it used a huge all-star cast of notable actors and actresses.  The title role was played by Natalie Gregory, who wore a blonde wig for this miniseries.  "Alice in Wonderland" was first telecast December 9, 1985, (part one) and December 10, 1985 (part two), at 8:00pm EST on CBS.

The Return of the Shaggy Dog: The Return of the Shaggy Dog is a 1987 American two-part made-for-television comedy film produced by Walt Disney Television.  The film is set in the 17 years between the events portrayed in "The Shaggy Dog" (1959) and "The Shaggy D.A." (1976).  It was broadcast on November 1 and 8, 1987 as a "Disney Sunday Movie" presentation on ABC.

Lewis Carroll: A Biography: Lewis Carroll: A Biography is a 1995 biography of author Lewis Carroll by Morton N. Cohen, first published by Knopf, later by Macmillan.  It is generally considered to be the definitive scholarly work on Carroll's (real name Charles Lutwidge Dodgson) life.  Cohen's approach is mainly chronological, with some chapters grouped by theme, such as those on Carroll's religion, his love of little girls, and his guilty feelings.  Cohen, a Carroll scholar for 30 years, opts to use Dodgson's first name, Charles, throughout the work, because it "seems most appropriate in a book dealing with the intimacy of his life".

In the Shadow of the Dreamchild: In the Shadow of the Dreamchild: A New Understanding of Lewis Carroll is a 1999 book by British author Karoline Leach that posited the concept of the "Carroll Myth": the idea that many of the most famous aspects of Lewis Carroll's biography, including his supposed adoration of Alice Liddell, are more legend than fact.

The Boy Who Talked to Badgers: "The Boy Who Talked to Badgers" is a 1975 two-part made-for-television adventure film directed by Gary Nelson, starring Christian Juttner and Carl Betz which originally aired on "The Wonderful World of Disney" on September 14 and 21, 1975.  It was adapted from Allan W. Eckert's book "Incident at Hawk's Hill", which was runner-up for a Newbery Award.

Natalie Palamides: Natalie Palamides (born January 6, 1990) is an American actress, comedian and writer who has been known for appearing on BuzzFeed.  She has written "My Name Is Vivienne," "Freaks of Nature" and "Burning Bridges."  She stars as Buttercup in the new "Powerpuff Girls" series that airs on Cartoon Network.  The show was released in April 4, 2016 in the United States.  She reprised her role as Buttercup in the "Uncle Grandpa" episode "Pizza Eve" during the Grampies short.  Palamides has played Kathy Murch in the comedy-horror film "Freaks of Nature" in October 30, 2015.

Spot Marks the X: Spot Marks the X is a 1986 Disney Channel Original Movie that starred Mike the Dog (from "Down and Out in Beverly Hills") as Capone/Astro, Barret Oliver (from "The Neverending Story", "Frankenweenie", "D.A.R.Y.L", and "Cocoon") as Ken, and Natalie Gregory (from "Alice in Wonderland (1985 version)", "Oliver & Company", and "Cranium Command") as Kathy, who, unlike her role as Alice in the aforementioned 1985 version, is seen with her real hair in this movie, which is brunette.  It was produced by Gregory Harrison's production company, The Catalina Production Group, Ltd. in association with Walt Disney Television.

Question: When was the movie that was a two-part made-for-television film adapted from a Lewis Carroll book, that was also a Disney movie was Natalie Gregory, who played Kathy in Spot Marks the X also appear in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released or first broadcast."
    },
    "film_type": {
      "type": "string",
      "description": "Describes the format of the film, e.g., 'made-for-television film'."
    },
    "is_two_part": {
      "type": "boolean",
      "description": "Indicates if the film was broadcast in two parts."
    },
    "adaptation_details": {
      "type": "object",
      "properties": {
        "adapted_from_author": {
          "type": "string",
          "description": "The author whose work the film was adapted from."
        },
        "source_books": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The specific books the film was adapted from."
        }
      },
      "required": [
        "adapted_from_author",
        "source_books"
      ],
      "additionalProperties": false
    },
    "main_cast_member": {
      "type": "object",
      "properties": {
        "actress_name": {
          "type": "string",
          "description": "The name of the main actress in this film."
        },
        "role_played": {
          "type": "string",
          "description": "The role played by the actress in this film."
        },
        "other_notable_role": {
          "type": "object",
          "properties": {
            "movie_title": {
              "type": "string",
              "description": "The title of another movie the actress appeared in, as mentioned in the question."
            },
            "role_name": {
              "type": "string",
              "description": "The role played by the actress in the other notable movie."
            }
          },
          "required": [
            "movie_title",
            "role_name"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "actress_name",
        "role_played",
        "other_notable_role"
      ],
      "additionalProperties": false
    },
    "broadcast_information": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "part_number": {
            "type": "integer",
            "description": "The part number of the broadcast."
          },
          "broadcast_date": {
            "type": "string",
            "format": "date",
            "description": "The date of the broadcast for this part."
          },
          "broadcast_time": {
            "type": "string",
            "description": "The time of the broadcast for this part."
          },
          "network": {
            "type": "string",
            "description": "The television network that broadcast this part."
          }
        },
        "required": [
          "part_number",
          "broadcast_date",
          "broadcast_time",
          "network"
        ],
        "additionalProperties": false
      },
      "description": "Details about the film's broadcast, including parts, dates, times, and networks."
    },
    "first_broadcast_date": {
      "type": "string",
      "format": "date",
      "description": "The date of the first part's broadcast, which is the answer to the question."
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "film_type",
    "is_two_part",
    "adaptation_details",
    "main_cast_member",
    "broadcast_information",
    "first_broadcast_date"
  ],
  "additionalProperties": false
}
