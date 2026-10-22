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
Uganda Be Kidding Me: Live: Uganda Be Kidding Me Live is a Netflix stand-up comedy special by Chelsea Handler in support of her "New York Times" Best-Selling book of the same name.  It was filmed in Chicago at the Harris Theater on June 20, and released on Netflix on October 10, 2014.

Sick and Tired (2006): Sick and Tired is a stand-up comedy special written and performed by actress and comedian Wanda Sykes.  The show premiered on October 14, 2006 on HBO.  It is directed by Michael Drumm and was filmed in front of a live audience at the Moore Theatre in Seattle, WA.  The show was nominated for the 2007 Emmy Award for Outstanding Variety, Music or Comedy Special.  According to Linda Mizejewski, a Women, Gender and Sexuality Studies professor at Ohio State University, in her book, "Pretty/Funny: Women Comedians and Body Politics", the title of the special refers to the quote by Fannie Lou Hamer, "I am sick and tired of being sick and tired."

I'ma Be Me (2009): I’ma Be Me is a stand-up comedy special written and performed by actress and comedian Wanda Sykes.  The show premiered on October 10, 2009 on HBO.  It was directed by Beth McCarthy-Miller and was filmed in front of a live audience at the Warner Theatre in Washington, D.C.  The show was nominated for two 2010 Emmy Awards including Outstanding Variety, Music or Comedy Special and Outstanding Writing for a Variety, Music or Comedy Special.  In a review of the performance Rip Empson of the Huffington Post says, “Sykes shows that her swagger hasn’t been slowed by maturity or motherhood."

Night After Night with Allan Havey: Night After Night with Allan Havey was a late night talk show which aired on The Comedy Channel and, later, Comedy Central from 1989 to 1992.  The show featured the stream of consciousness of host Allan Havey, and other departures from the standard late-night talk show format.  Havey's sidekick was Nick Bakay, who moved on to act as sidekick on Dennis Miller's short-lived late night talk show.

The Week Show: The Week Show is a television late night talk show sketch comedy program on Bite TV in Canada.  It originally ran from December 2008 to mid-2010.  The show is hosted by Matt Chin and Ricky Thompson, who started on an internet late night talk show "My Show with Matt Chin" online in 2001.

Late-night talk show: A late-night talk show is a genre of talk show popular in the United States, where the format originated.  It is generally structured around humorous monologues about the day's news, guest interviews, comedy sketches and music performances.  The late-night talk show format was popularized, though not invented, by Johnny Carson with "The Tonight Show Starring Johnny Carson" on NBC.  Typically the show's host conducts interviews from behind a desk, while the guest is seated on a couch.  Many late night talk shows feature a house band which generally performs cover songs for the studio audience during commercial breaks and occasionally will back up a guest artist.

David Letterman: David Michael Letterman (born April 12, 1947) is an American television host, comedian, writer, and producer.  He hosted a late night television talk show for 33 years, beginning with the February 1, 1982 debut of "Late Night with David Letterman" on NBC, and ending with the May 20, 2015 broadcast of "Late Show with David Letterman" on CBS.  In total, Letterman hosted 6,028 episodes of "Late Night" and "Late Show", surpassing friend and mentor Johnny Carson as the longest-serving late night talk show host in American television history.  In 1996 Letterman was ranked 45th on "TV Guide"' s 50 Greatest TV Stars of All Time.

Jebb Fink: Jebb Fink is an American-Canadian stand-up comedian and television personality.  Best known as a reporter and host for "the Big Breakfast" on A-Channel, Calgary.  He won a Gemini as co-creator of the CBC comedy "An American in Canada" and was a weather presenter on "Your City" for City TV Calgary, he also hosted the short-lived late night talk show "Global Late Night" for the Global Television Network in 2004.

Chelsea Handler: Chelsea Joy Handler (born February 25, 1975) is an American comedian, actress, writer, television host, and producer.  She hosted the late-night talk show "Chelsea Lately" on the E! network from 2007 to 2014, and released a documentary series, "Chelsea Does", on Netflix in January 2016.  In 2012, "Time" named Handler one of the 100 most influential people in the world on their annual "Time" 100 list.

List of Jimmy Fallon games and sketches: The following is a list of recurring games, sketches, and other comedy routines from the NBC late night talk show "The Tonight Show Starring Jimmy Fallon", and its predecessor, "Late Night with Jimmy Fallon".  The sketches feature host Jimmy Fallon, house band The Roots, announcer/sidekick Steve Higgins, the show's writers, celebrity guests, and audience members.  Most of the skits below appeared only on "Late Night", while some have carried over to the "Tonight Show".

Question: Uganda Be Kidding Me: Live is a Netflix stand-up comedy special by an American comedian who hosted what late night talk show on E! from 2007-2014?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comedian_name": {
      "type": "string",
      "description": "The name of the comedian who performed the stand-up special."
    },
    "stand_up_special_name": {
      "type": "string",
      "description": "The title of the stand-up comedy special."
    },
    "late_night_talk_show": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the late-night talk show."
        },
        "network": {
          "type": "string",
          "description": "The television network the talk show aired on."
        },
        "start_year": {
          "type": "integer",
          "description": "The year the talk show began."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the talk show ended."
        }
      },
      "required": [
        "title",
        "network",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comedian_name",
    "stand_up_special_name",
    "late_night_talk_show"
  ],
  "additionalProperties": false
}
