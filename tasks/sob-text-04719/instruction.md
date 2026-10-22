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
North Square: North Square is a British television drama series written and created by Peter Moffat, and broadcast by Channel 4 from 18 October to 20 December 2000.  Starring an ensemble cast, including Phil Davis, Rupert Penry-Jones, Helen McCrory and Kevin McKidd, the programme is set around the practice of a barristers' chambers in Leeds.  The series was filmed in and around the real life Park Square, Leeds.  This is the area in the city where the majority of barristers' chambers are concentrated.

Persuasion (2007 film): Persuasion is a 2007 British television film adaptation of Jane Austen's novel "Persuasion".  It was directed by Adrian Shergold and the screenplay was written by Simon Burke.  Sally Hawkins stars as the protagonist Anne Elliot, while Rupert Penry-Jones plays Frederick Wentworth.  Eight years prior to the film's beginning, Anne was persuaded to reject Wentworth's proposal of marriage.  Now 27 and unmarried, Anne re-encounters Wentworth, who has made his fortune in the Napoleonic Wars and is looking for a wife—anyone but Anne, whom he has not forgiven for rejecting him all those years ago.

Spooks (series 3): The third series of the British spy drama television series "Spooks" (known as MI-5 in the United States) began broadcasting on 11 October 2004 on BBC One, before ending on 13 December 2004.  It consists of ten episodes which continue to follow the actions of Section B, a counter-terrorism division of the British Security Services (MI5).  It also sees the departure of three principal characters: Tom Quinn (Matthew Macfadyen) is decommissioned in the second episode, Zoe Reynolds (Keeley Hawes) is exiled to Chile in the sixth episode, and Danny Hunter (David Oyelowo) is killed in the series finale.  In addition to Macfadyen, Hawes and Oyelowo, Peter Firth, Rupert Penry-Jones, Nicola Walker, Hugh Simon, Shauna Macdonald and Rory MacGregor are listed as the main cast.

The 39 Steps (2008 film): The 39 Steps is a 2008 British television adventure thriller feature-length adaptation of the John Buchan novel "The Thirty-Nine Steps" produced by the BBC.  It was written by Lizzie Mickery, directed by James Hawes, and filmed on location in Scotland, starring Rupert Penry-Jones, Lydia Leonard, David Haig, Eddie Marsan, and Patrick Malahide.  Following three screen versions of the novel and the 1952 and 1977 television adaptations of "The Three Hostages", Penry-Jones became the sixth actor to portray Hannay on screen.  This adaptation is set on the eve of the First World War and sees mining engineer Richard Hannay caught up in an espionage conspiracy following the death of a British spy in his flat.

Spooks (series 7): The seventh series of the BBC espionage television series "Spooks" (known as MI-5 in the United States) began broadcasting on 27 October 2008 on BBC One before ending on 8 December 2008 on the same channel, and consists of eight episodes, two fewer than previous series.  It follows the actions of Section D, a counter-terrorism division in MI5.  The primary storyline involves Sugarhorse, a top secret operation set up by MI5 during the final years of the Cold War, and a mole working for the FSB who intends to leak the operation to the Russians.  Peter Firth, Rupert Penry-Jones, Hermione Norris, Richard Armitage, Miranda Raison, Gemma Jones, Hugh Simon and Alex Lanipekun are credited as the main cast.

Charlotte Gray (film): Charlotte Gray is a 2001 British–Australian–German film drama directed by Gillian Armstrong.  The screenplay was adapted from Sebastian Faulks' novel with the same title.  It is set in Vichy France during World War II.  The film stars Cate Blanchett, James Fleet, Abigail Cruttenden, Rupert Penry-Jones, Michael Gambon and Billy Crudup.

Crown for Christmas: Crown for Christmas is a 2015 American made-for-television romantic comedy film starring Danica McKellar, Rupert Penry-Jones.  The film premiered on Hallmark Channel on November 27, 2015.

A Little Chaos: A Little Chaos is a 2014 British period drama film directed by Alan Rickman.  The story was conceived by Allison Deegan and she co-wrote the screenplay along with Rickman and Jeremy Brock.  The film stars Kate Winslet, Matthias Schoenaerts, Alan Rickman, Stanley Tucci, Helen McCrory, Steven Waddington, Jennifer Ehle and Rupert Penry-Jones.  The film was financed by the Lionsgate UK and produced by BBC Films.  It was the second film directed by Rickman, after his 1997 directorial debut "The Winter Guest".  It was the second collaboration of Rickman and Winslet after their 1995 film "Sense and Sensibility".  Production took place in London in mid 2013.  The film had its world premiere at the 2014 Toronto International Film Festival as the closing night film on 13 September 2014.

Rupert Penry-Jones: Rupert William Penry-Jones (born 22 September 1970) is an English actor, best known for his roles as Adam Carter in the BBC One spy drama series "Spooks", Clive Reader QC in the BBC One legal drama "Silk", policeman DI Joseph Chandler in the ITV murder mystery series "Whitechapel", and Mr. Quinlan in the FX horror series "The Strain".

The Priory (play): The Priory is a play by Michael Wynne that opened at the downstairs theatre of the Royal Court Theatre in London in 2009.  The production starred Jessica Hynes, Rupert Penry-Jones, Charlotte Riley, Alastair Mackenzie, Joseph Millson and Rachael Stirling.  After receiving good reviews, its run was extended.  Michael Wynne won the Olivier Award for 'Best New Comedy' for "The Priory".  Stirling was nominated for a Laurence Olivier Award for Best Performance in a Supporting Role for her role as Rebecca.

Question: Persuasion stars Rupert Penry-Jones and who else

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "main_actor_queried": {
      "type": "string",
      "description": "The name of the actor whose co-stars are being identified."
    },
    "co_stars": {
      "type": "array",
      "description": "A list of other actors who starred in the film alongside the main actor.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "film_title",
    "main_actor_queried",
    "co_stars"
  ],
  "additionalProperties": false
}
