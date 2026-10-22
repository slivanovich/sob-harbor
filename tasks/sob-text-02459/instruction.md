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
Jonathan Kurtiss: Jonathan Kurtiss is a fictional character in the Australian Channel Seven drama series "Winners & Losers", played by Damien Bodie.  Jonathan made his debut screen appearance in the pilot episode "Covert Aggression in Netball", broadcast on 22 March 2011.  Bodie secured the role while working in the United States and returned to Melbourne to play Jonathan.

Packed to the Rafters (season 5): The fifth season of "Packed to the Rafters", an Australian drama television series premiered on 17 April 2012 on the Seven Network.  22 episodes have been ordered for Season five.  The Seven network put the series on hiatus again on June 19, 2012 after 10 episodes, despite previously promising that viewers would see a full season run.  The show returned on 29 January 2013 with episode 11, accompanied by an increase in viewers compared to previous episodes of the season.

Winners &amp; Losers: Winners & Losers is an Australian television drama series first broadcast on the Seven Network on 22 March 2011.  It was created by the producers of "Packed to the Rafters" and is aired in the show's former time slot.  "Winners & Losers" focuses on the lives of four women living in Melbourne, after they win a large amount of money in the Oz Lotto.  Seven renewed "Winners & Losers" for a second season in July 2011 and it began airing from 26 June 2012.  Two months later, it was announced the series had been renewed for a third season.  A fourth season was confirmed on 19 December 2013.  A fifth season was confirmed on 3 December 2014.

The Balanced Particle Freeway: The Balanced Particle Freeway is a 1997 Australian TV movie starring Damien Bodie.

Damien Bodie: Damien Bodie (born 2 January 1985) is an Australian actor.  Best known for his role as "Dylan Timmins" in Neighbours.

Dylan Timmins: Dylan Kim Timmins is a fictional character from the Australian soap opera "Neighbours", played by Damien Bodie.  He made his first appearance during the episode broadcast on 3 February 2005.  Dylan is the older brother of Stingray, Janae and Bree Timmins.  Dylan became the protégé of Paul Robinson.  Brodie chose to the leave the show in 2006 and he made his last appearance on 30 March 2007.

Packed to the Rafters: Packed to the Rafters is an Australian family-oriented drama/comedy television program which premiered on the Seven Network on Tuesday 26 August 2008 at 8:30 pm.  The show continued on Tuesdays in this timeslot for its entire run.  The drama series features a mix of lighthearted comedy woven through the plot.  It revolves around the Rafter family facing work pressures and life issues, whilst also tackling serious social issues.  The Logie award winning series was the highest rating to screen on the Seven Network in 2008, and the show has consistently been among the top 5 shows of the year throughout its run in Australia.

Daniel Collopy: Daniel Collopy (born 1 February 1978) is an Australian actor.  His first television role was in 2000 as the character of Sean Edwards in the long-running Australian soap "Neighbours".  Following this Collopy was offered a regular role in another long-running Australian soap Home and Away where he played lifeguard turned town mayor Josh West from 2001 until 2003 with further guest appearances in both 2005 and 2006.  In 2003, he was nominated for a Logie Award being for Logie Award for Most Popular New Male Talent for his role in Home and Away.  Collopy has guest starred in Packed to the Rafters, the police drama series City Homicide, and the comedy series Jesters.

Linden Wilkinson: Linden Wilkinson is an Australian film, television and theatre actress and writer.  She is perhaps best known for her recurring role in soap opera "Home and Away" playing 'The Believers' cult leader Mumma Rose.  Her other roles include appearances on "Prisoner: Cell Block H", "A Country Practice", "Water Rats", and "Packed to the Rafters".  Wilkinson spends most of her time acting in and writing theatre productions, she has worked extensively in State Theatre Companies in Adelaide, Melbourne and Auckland, some of her theatre credits are "A Day in December", "Family Favourites", "Happy House Show", "Nice Girls" and "Night of the Missing Bridegroom".  She bagan writing and script-editing for television series such as "Ocean Girl" and "Outriders", and she has also written for two feature films, "Moon River", an adaptation of the novel by Brenda Walker of the same name, and "Pearls", a romantic comedy.

Jonathon Dutton: Jonathon Dutton (born 23 August 1982) is an Australian actor and director.  From 1998 to 2002, Dutton played Tad Reeves in "Neighbours".  He later returned to the show as a director.  Dutton has also appeared in "MDA", "Two Pints of Lager and a Packet of Crisps" and "Packed to the Rafters".

Question: What show that starred Damien Bodie was created by the producers of "packed to the Rafters"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_title": {
      "type": "string",
      "description": "The title of the television series that meets the criteria."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor who starred in the show."
        },
        "character_name": {
          "type": "string",
          "description": "The name of the character played by the actor in the show."
        }
      },
      "required": [
        "actor_name",
        "character_name"
      ],
      "additionalProperties": false
    },
    "producer_origin": {
      "type": "object",
      "properties": {
        "created_by_producers_of_show": {
          "type": "string",
          "description": "The title of the show whose producers created the answer show."
        },
        "is_created_by_specified_producers": {
          "type": "boolean",
          "description": "Indicates if the show was created by the producers of the specified show."
        }
      },
      "required": [
        "created_by_producers_of_show",
        "is_created_by_specified_producers"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "show_title",
    "actor_details",
    "producer_origin"
  ],
  "additionalProperties": false
}
