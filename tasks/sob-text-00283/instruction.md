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
2003 Bonnaroo Music Festival: The festival ran June 13–15, and 80,000 attended.  In 2003, The Bonnaroo organizers planned a festival called Bonnaroo Northeast to take place in Riverhead, Long Island, New York.  This festival, as well as the Field Day Festival, another festival to take place at the same site, were cancelled, however, in the weeks leading up to the event due to concern about securing permits in time.

Teknival: Teknivals (the word is a portmanteau of the words tekno and festival) are large free parties which take place worldwide.  They take place most often in Europe and are often illegal under various national or regional laws.  They vary in size from dozens to thousands of people, depending on factors such as accessibility, reputation, weather, and law enforcement.  The parties often take place in venues far away from residential areas such as squatted warehouses, empty military bases, beaches, forests or fields.  The teknival phenomenon is a grassroots movement which has grown out of the rave, UK traveller and Burning Man scenes and spawned an entire subculture.  Summer is the usual season for teknivals.

CMLL Super Viernes: CMLL Super Viernes (Spanish for "CMLL Super Friday") is the Mexican professional wrestling promotion Consejo Mundial de Lucha Libre's banner event that takes place every Friday in Arena México in Mexico City, Mexico.  The shows take place every Friday all year long, except when CMLL schedules a "Super Show" or a Pay-Per-View (PPV) to take its place since all CMLL PPVs and Super Shows take place on Friday nights in Arena México.

Aniversario: Never Compromise: Aniversario: Never Compromise was a professional wrestling internet pay-per-view (iPPV) event produced by the Chikara promotion, that took place on June 2, 2013, at the Trocadero Theatre in Philadelphia, Pennsylvania.  The event marked Chikara's fourth iPPV, third to take place at the Trocadero Theatre and the promotion's only event to take place in Philadelphia in 2013.  Much like the previous iPPV, Under the Hood, Aniversario: Never Compromise also aired through Smart Mark Video.  Aniversario: Never Compromise celebrated Chikara's eleventh anniversary and was the first anniversary event to take place on iPPV; in the past, the promotion had celebrated its anniversaries with weekends of two shows.  The event saw all three Chikara championships being defended with one title change, where Pieces of Hate (Jigsaw and The Shard) defeated 3.0 (Scott Parker and Shane Matthews) for the Campeonatos de Parejas.  Another major match during the event saw former Campeones de Parejas, Amasis and Ophidian, end their nineteen-month storyline rivalry in a Sarcophagus match.  The event concluded with a major storyline development, where Chikara's authority figure Wink Vavasseur ended the event and shut down the promotion, while the main event was still going on in the ring, leading to the promotion going inactive for a full year.

2015–17 Irish gangland feud: A major feud between two criminal gangs in the Republic of Ireland has killed ten people.  The Hutch gang, led by Gerry Hutch, and the Kinahan gang, led by Christy Kinahan, are the main participants.

2016 WTA 125K series: The WTA 125K series is the secondary professional tennis circuit organised by the Women's Tennis Association.  The 2016 WTA 125K series calendar consists of eight tournaments, each with a total prize fund of $125,000.  After 2015, the Nanchang event was upgraded to a WTA International level tournament, and with new events starting in San Antonio, West Hempstead and Bol.  The planned tournament in West Hempstead was then cancelled, and the tournament scheduled to take place in Carlsbad, California was moved to Oahu, Hawaii.  Following the death of the Thai king Bhumibol Abdulyadej, the event due to take place in Hua Hin was also cancelled, in accordance with Thai tradition that sporting events cannot take place in the month after a monarch's death.

Lindenstraße: Lindenstraße (literally "Lime Street") is a German television drama series, broadcast by Das Erste.  The first episode aired on 8 December 1985 and since then new episodes have aired weekly.  Its current timeslot on Das Erste is Sundays at 18:50.  The events of the Sunday episode usually take place on the Thursday before the show, based on the TV station's original plan of airing the episodes Thursday night.  Prior of the start of the show, the timeslot was switched to Sunday evening but the Thursday remained the day the events usually take place as the show shall feature the daily life routine of the protagonists on a working day.  Exceptions are the so-called holiday episodes that take place on Sunday, such as for Christmas and Easter and also on important election days (especially the election to the German Bundestag).

Shooting of Gareth Hutch: Gareth Hutch was shot dead on Tuesday 24 May 2016.  He was a nephew of Gerry Hutch.  He was also a cousin of Gary Hutch and a nephew of Eddie Hutch Snr.

Shooting of Eddie Hutch Snr: The shooting of Eddie Hutch Snr occurred on 8 February 2016.  Eddie was the brother of Gerry Hutch, the leader of the Hutch gang, which was in a feud with the Kinahan gang, led by Christy Kinahan.  The feud of the two criminal gangs, called the 2015–16 Irish gangland feud, in the Republic of Ireland resulted in the deaths of ten people.

Gerry Hutch: Gerry Hutch (born 1963) is an Irish criminal.  He was the prime suspect for two of the biggest armed robberies in Irish history.  Known for leading a "disciplined, ascetic lifestyle" since leaving prison in 1985, he was christened "The Monk" by Veronica Guerin, an investigative journalist who applied nicknames to Ireland's crime bosses before being assassinated in 1996.

Question: How long after the assasination of Gerry Hutch did the shoothing of his brother take place?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_of_interest": {
      "type": "object",
      "description": "Details about the shooting event mentioned in the question.",
      "properties": {
        "victim_name": {
          "type": "string",
          "description": "The name of the person who was shot."
        },
        "event_date": {
          "type": "string",
          "format": "date",
          "description": "The date the shooting occurred."
        }
      },
      "required": [
        "victim_name",
        "event_date"
      ],
      "additionalProperties": false
    },
    "related_person_details": {
      "type": "object",
      "description": "Information about Gerry Hutch, the person whose assassination date is requested.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the related person."
        },
        "relationship_to_victim": {
          "type": "string",
          "description": "The relationship of this person to the victim of the shooting."
        },
        "was_assassinated_in_context": {
          "type": "boolean",
          "description": "Indicates if this person was assassinated according to the provided context."
        }
      },
      "required": [
        "name",
        "relationship_to_victim",
        "was_assassinated_in_context"
      ],
      "additionalProperties": false
    },
    "duration_calculable": {
      "type": "boolean",
      "description": "Indicates whether the duration requested in the question can be calculated based on the provided context."
    }
  },
  "required": [
    "event_of_interest",
    "related_person_details",
    "duration_calculable"
  ],
  "additionalProperties": false
}
