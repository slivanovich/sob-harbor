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
Le Week-End: Le Week-End is a 2013 British-French drama film directed by Roger Michell and written by Hanif Kureishi.  The film is the fourth collaboration between Michell and Kureishi, who both began developing the story seven years prior during a weekend trip to Montmartre.  It was screened in the Special Presentation section at the 2013 Toronto International Film Festival.

My Night with Reg (film): My Night with Reg is a 1996 British film adapted from the Kevin Elyot play of the same title, and directed by Roger Michell.

Hyde Park on Hudson: Hyde Park on Hudson is a 2012 British biographical historical comedy-drama film directed by Roger Michell.  The film stars Bill Murray as Franklin D. Roosevelt and Laura Linney as Margaret "Daisy" Suckley, a cousin and childhood friend of the President.  It was based on Suckley’s private journals and diaries, discovered after her death, and fictionally dramatizes her close personal relationship with Roosevelt, and the 1939 visit of King George VI and Queen Elizabeth to Roosevelt's country estate, Hyde Park.

Notting Hill (film): Notting Hill is a 1999 British romantic comedy film set in Notting Hill, London, released on 21 May 1999.  The screenplay was by Richard Curtis, who had written "Four Weddings and a Funeral" (1994), and the film was produced by Duncan Kenworthy and directed by Roger Michell.  The film stars Hugh Grant, Julia Roberts, Rhys Ifans, Emma Chambers, Tim McInnerny, Gina McKee, and Hugh Bonneville.

Enduring Love (film): Enduring Love is a 2004 British film directed by Roger Michell with screenwriter Joe Penhall, based on the novel of the same name by Ian McEwan.  The story concerns two strangers who become dangerously close after witnessing a deadly accident.  It stars Daniel Craig, Rhys Ifans and Samantha Morton with Bill Nighy, Susan Lynch and Corin Redgrave.

My Cousin Rachel (2017 film): My Cousin Rachel is a 2017 romantic drama film, written and directed by Roger Michell, based upon the 1951 novel of the same name by Daphne du Maurier.  It stars Rachel Weisz, Sam Claflin, Iain Glen, Holliday Grainger and Pierfrancesco Favino.  It was shot in England and Italy in spring 2016, and is about a young man in Cornwall who meets the wife of his older cousin, suspecting her of having been responsible for his death.

Kevin Loader: Kevin Loader is a British film and television producer.  Since 1996, he and co-owner Roger Michell have run a London-based production company, Free Range Films, through which the pair have made several feature films directed by Michell, including "The Mother", "Enduring Love", "Venus", "Hyde Park on Hudson", and "Le Week-end".  Their most recent film is an adaptation by Michell of Daphne Du Maurier's "My Cousin Rachel".  The company is also developing and producing film and television projects with other directors.  Loader was awarded the Bafta for Best Television Serial in 2015 for "The Lost Honour of Christopher Jefferies".

The Mother (film): The Mother is a 2003 British film directed by Roger Michell.

Morning Glory (2010 film): Morning Glory is a 2010 American comedy film directed by Roger Michell and written by Aline Brosh McKenna.  It stars Rachel McAdams, Harrison Ford and Diane Keaton, with Patrick Wilson, John Pankow and Jeff Goldblum.  The plot revolves around young and devoted morning television producer Becky Fuller (McAdams), who is hired as an executive producer on the long-running morning show "DayBreak", at a once-prominent but currently failing station in New York City.  Eager to keep the show on air, she recruits a former news journalist and anchor (Ford) who disapproves of co-hosting a show that does not deal with real news stories.

My Night with Reg: My Night with Reg is a play by British playwright Kevin Elyot which was produced in 1994 by the Royal Court Theatre, London, directed by Roger Michell.  The production later transferred to the West End.

Question: Which company owned by British Film producer Kevin Loader and his partner Roger Michell produced the 2017 film My Cousin Rachel?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "production_company_name": {
      "type": "string",
      "description": "The name of the production company."
    },
    "company_owners": {
      "type": "array",
      "description": "A list of individuals who own the company.",
      "items": {
        "type": "object",
        "properties": {
          "owner_name": {
            "type": "string",
            "description": "The name of an owner."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the owner."
          }
        },
        "required": [
          "owner_name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "film_produced": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film produced."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "production_company_name",
    "company_owners",
    "film_produced"
  ],
  "additionalProperties": false
}
