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
Restless (2011 film): Restless is a 2011 British-American romantic comedy-drama film directed by Gus Van Sant and written by Jason Lew.  It stars Henry Hopper and Mia Wasikowska.  Shot in Portland, Oregon, United States, and produced by Bryce Dallas Howard, Ron Howard and Brian Grazer for Sony Pictures Classics and Imagine Entertainment, it was released on September 16, 2011.  It was screened in the Un Certain Regard section at the 2011 Cannes Film Festival on May 12.

Rebecca Hazlewood: Rebecca Hazlewood (born 1977) is an English actress of mixed English and Indian descent.  Hazlewood was born in Wales and grew up in Kingswinford in the West Midlands and studied English Literature at Bretton Hall.  She is best known in the UK for her roles as Beena Shah in "Crossroads" and Arun Parmar in "Bad Girls", and in the US for her role as Asha in the NBC primetime comedy series "Outsourced".  Outsourced was cancelled after completing a full season in 2011.  Her other roles include Talia Ahmed in the ITV series "Second Sight" alongside Clive Owen, in the "Masters of the Universe" BBC1 week-long series in January 2010 as college lecturer Sia and the 2001 British Film 4 feature "Dog Eat Dog" with David Oyelowo, Gary Kemp and Ricky Gervais.  In 2006 she featured as Beth in "Meeting Helen" with Madeleine Potter and Emily Woof which was filmed by DP Christopher Doyle.  In Kissing Cousins the movie she appeared as a lead role.

Vanessa Howard: Vanessa Howard (born Vanessa Tolhurst, 10 October 1948, Shoreham-by-Sea, United Kingdom-23 November 2010), later known as Vanessa Chartoff, was a British film actress and professional backup singer.  Howard starred primarily in exploitation and horror films.  She is perhaps best known for her starring roles in "The Blood Beast Terror" and "Mumsy, Nanny, Sonny and Girly"; the latter has since become a cult movie.  The box-office failure of her later projects resulted in her decision to give up acting.

Willow (film): Willow is a 1988 British-American high fantasy film directed by Ron Howard, produced and with a story by George Lucas, and starring Warwick Davis, Val Kilmer, Joanne Whalley, Jean Marsh, and Billy Barty.  Davis plays the eponymous lead character and hero: a reluctant farmer who plays a critical role in protecting a special baby from a tyrannical queen who vows to destroy her and take over the world in a high fantasy setting.

The Lord of the Rings (1978 film): The Lord of the Rings is a 1978 American-British animated high fantasy film directed by Ralph Bakshi.  It is an adaptation of J. R. R. Tolkien's high fantasy epic "The Lord of the Rings", comprising "The Fellowship of the Ring" and the first half of "The Two Towers".  Set in Middle-earth, the film follows a group of hobbits, elves, men, dwarves, and wizards who form a fellowship.  They embark on a quest to destroy the One Ring made by the Dark Lord Sauron, and ensure his destruction.

Frost/Nixon (film): Frost/Nixon is a 2008 British-American historical drama film based on the 2006 play of the same name by Peter Morgan, who also adapted the screenplay.  The film tells the story behind the Frost/Nixon interviews of 1977.  The film was directed by Ron Howard and produced for Universal Pictures by Howard, Brian Grazer of Imagine Entertainment and Tim Bevan and Eric Fellner of Working Title Films, and received five Academy Award nominations, including Best Picture, Best Actor and Best Director.

Jean Marsh: Jean Lyndsey Torren Marsh, {'1': ", '2': ", '3': ", '4': "} (born 1 July 1934) is an English actress and writer.  Marsh co-created and starred in the ITV series "Upstairs, Downstairs" (1971–75), for which she won the 1975 Emmy Award for Outstanding Lead Actress in a Drama Series for her performance as Rose Buck.  She later reprised the role in the BBC's revival of the series (2010–12).  Marsh also co-created the television series "The House of Eliott" in 1991.  Her film appearances include "Cleopatra" (1963), "Frenzy" (1972), "The Changeling" (1980), "Return to Oz" (1985), "Willow" (1988) and "Monarch" (2000).

Cotton Candy (film): Cotton Candy is a 1978 American made-for-television drama film directed by Ron Howard and broadcast on NBC.  It is also known as Ron Howard's Cotton Candy.

Rance Howard: Rance Howard (born November 17, 1928) is an American actor who has starred in film and on television.  He is the father of actor and filmmaker Ron Howard and actor Clint Howard, and grandfather of the actress Bryce Dallas Howard.

Keeley Hawes: Keeley Clare Julia Hawes (born 10 February 1976) is an English actress.  She starred in the film version of "The Last September" (1999) and has voiced roles in video games, such as Lara Croft in several of the "Tomb Raider" games.  She is also known for her roles as Kitty Butler in "Tipping the Velvet", Zoe Reynolds in "Spooks" (2002–2004), Alex Drake in "Ashes to Ashes" (2008–2010), Lady Agnes in the 2010 reboot of "Upstairs, Downstairs", Detective Inspector Lindsay Denton in the second and third series of "Line of Duty" (2014–2016), as a mother in search of her abducted child in the BBC series "The Missing", and as Louisa Durrell in the ITV series "The Durrells".

Question: This British-American high fantasy film directed by Ron Howard starred an English actress and writer who co-created and starred in what ITV series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "director": {
          "type": "string"
        },
        "genre": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "director",
        "genre",
        "release_year"
      ],
      "additionalProperties": false
    },
    "actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "is_writer": {
          "type": "boolean"
        }
      },
      "required": [
        "name",
        "nationality",
        "is_writer"
      ],
      "additionalProperties": false
    },
    "itv_series": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "co_created_by_actress": {
          "type": "boolean"
        },
        "actress_role": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "co_created_by_actress",
        "actress_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film",
    "actress",
    "itv_series"
  ],
  "additionalProperties": false
}
