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
Alan Ayckbourn: Sir Alan Ayckbourn, CBE (born 12 April 1939) is a prolific English playwright and director.  He has written and produced more than seventy full-length plays in Scarborough and London and was, between 1972 and 2009, the artistic director of the Stephen Joseph Theatre in Scarborough, where all but four of his plays have received their first performance.  More than 40 have subsequently been produced in the West End, at the Royal National Theatre or by the Royal Shakespeare Company since his first hit "Relatively Speaking" opened at the Duke of York's Theatre in 1969.

Michael Pennington: Michael Vivian Fyfe Pennington (born 7 June 1943) is a British actor, director and writer.  Together with director Michael Bogdanov, he founded the English Shakespeare Company in 1986 and was its Joint Artistic Director until 1992.  He has written ten books, directed in the UK, US, Romania and Japan, and is an Honorary Associate Artist of the Royal Shakespeare Company.

The Shakespeare Project: In October 1983, the Riverside Shakespeare Company, then New York City's only year-round professional Shakespeare theatre company, inaugurated "The Shakespeare Project", based at the theatre company's home on the Upper West Side of Manhattan, The Shakespeare Center.  "The Shakespeare Project" was the first major New York residency of actors from the Royal Shakespeare Company - with Edwin Richfield, Heather Canning, Christopher Ravenscroft, Jennie Stoller and John Kane (the later two from Peter Brook's "A Midsummer Night's Dream") - for a week of public workshops, panel discussions, seminars and performances at the company's Upper West Side theatre, The Shakespeare Center.  The event was launched at a luncheon in the Shakespeare Room of the Algonquin Hotel attended by Joseph Papp, Helen Hayes, Frank Rich, Gloria Skurski, W. Stuart McDowell, and members of the Royal Shakespeare Company in mid October 1983.  According to the "New York Times", over one thousand actors, students, teachers and stage directors, from the ages of 15 to 87, signed up for 22 sessions taught by some of the leading actors from London's Royal Shakespeare Company.

World Theatre Season: The World Theatre Season was a festival of foreign plays held annually at the Royal Shakespeare Company's Aldwych Theatre in London from 1964 to 1973, with a final season in 1975.  It originated as a one-off celebration in 1964 organised by Peter Daubeny and the Royal Shakespeare Company as part of the celebrations for William Shakespeare's quatercentenary.  In the 1950s, Peter Daubeny had presented foreign theatre companies, which gave him a knowledge of foreign theatre and served as a prelude to the World Theatre Seasons.  Seven companies appeared at this initial World Theatre Season: Comédie Française; Schiller-Theater; Peppino de Filippo's Italian Theatre; Abbey Theatre; Polish Contemporary Theatre; Greek Art Theatre; and Moscow Art Theatre.

Trevor Nunn: Sir Trevor Robert Nunn, CBE (born 14 January 1940) is an English theatre director.  Nunn has been the Artistic Director for the Royal Shakespeare Company, the Royal National Theatre, and, currently, the Theatre Royal, Haymarket.  He has directed dramas for the stage, like "Macbeth", as well as opera and musicals, such as "Cats" (1981) and "Les Misérables" (1985).

Twelfth Night (1996 film): Twelfth Night (also known as Twelfth Night: Or What You Will) is a 1996 British film adaptation of William Shakespeare's play, directed by Trevor Nunn and featuring an all-star cast.  Set in the late 20th century, it was filmed on location in Cornwall, including scenes shot at Padstow and at Lanhydrock House near Bodmin, with Orsino and his followers wearing uniforms that evoke the Austro-Hungarian Empire.

Bart Whiteman: Bart Whiteman (1948-March 14, 2006) was a Washington, D.C. theatre actor, director, and producer.  He founded the Source Theatre in 1977 and served as its artistic director until 1986.  He was influential in defining theatre in Washington as well as reviving 14th Street.  According to Christopher Henley, artistic director of the "Washington Shakespeare Company", "Bart was one of the half-dozen or so of the most seminal influences on and pioneers of what theatre in D.C. was and has become.  He was part of that synergy -- along with Joy [Zinoman, founding artistic director of the "Studio Theatre"] and Tony Abeson [founder and director of the Washington Theatre Laboratory] -- that really began the small professional theatre movement in D.C. in the late 1970s."  Trey Graham of the Washington City Paper said that the richness and diversity of modern-day Washington theatre "had a lot to do with his role as evangelist and cattle prod and crazy-ass visionary."  Whiteman left the Source Theater after an incident in which it produced "Fool for Love" and "A Streetcar Named Desire" without paying royalties.  Later, he became a theater teacher at Montgomery Bell Academy in Nashville, Tennessee and wrote editorials and theater reviews for "The Chattanoogan" in Chattanooga, Tennessee.

Leon Rubin: Professor Leon Rubin is a UK, Theatre Director, Theatre Management Consultant, Professor, Writer, and Director of East 15 Acting School, University of Essex.  He is a member of the Directors Guild of Great Britain and a Fellow of the Royal Society of Arts and a Fellow of the Royal Asiatic Society.  He was the first foreigner to be awarded an Honorary Professorship of GITIS Russian Theatre Academy, Moscow, in 1997.  He began his career as Assistant Director at the Royal Shakespeare Company, and has been Artistic Director of three major UK theatre companies: Lyric Theatre, Belfast, Watford Palace theatre the Bristol Old Vic and Associate at the Abbey Theatre, Dublin,

Bill Alexander (director): William Alexander Paterson (born 23 February 1948) known professionally as Bill Alexander is a British theatre director who is best known for his work with the Royal Shakespeare Company and as artistic director of Birmingham Repertory Theatre.  He currently works as a freelance, internationally as a theatre director and most recently as a director of BBC Radio 4 drama.

Royal Shakespeare Theatre: The Royal Shakespeare Theatre (RST) is a 1,040+ seat thrust stage theatre owned by the Royal Shakespeare Company dedicated to the English playwright and poet William Shakespeare.  It is located in the town of Stratford-upon-Avon – Shakespeare's birthplace – in the English Midlands, beside the River Avon.  The Royal Shakespeare and Swan Theatres re-opened in November 2010 after undergoing a major renovation known as the Transformation Project.

Question: Who wrote the play for which the 1996 film by the Artistic Director for the Royal Shakespeare Company is based?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_adaptation": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film adaptation."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the film's director."
            },
            "role_at_royal_shakespeare_company": {
              "type": "string",
              "description": "The director's role at the Royal Shakespeare Company."
            }
          },
          "required": [
            "name",
            "role_at_royal_shakespeare_company"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "title",
        "year",
        "director"
      ],
      "additionalProperties": false
    },
    "source_play": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the play the film is based on."
        },
        "author": {
          "type": "string",
          "description": "The author of the source play."
        }
      },
      "required": [
        "title",
        "author"
      ],
      "additionalProperties": false
    },
    "final_answer_author": {
      "type": "string",
      "description": "The name of the author of the play."
    }
  },
  "required": [
    "film_adaptation",
    "source_play",
    "final_answer_author"
  ],
  "additionalProperties": false
}
