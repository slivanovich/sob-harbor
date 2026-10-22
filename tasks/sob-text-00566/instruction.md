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
2011 murder of the Ding family: The 2011 murder of the Ding family occurred in Wootton, a suburb of Northampton, England, in late April.  Four members of the Ding familyProfessor Jifeng "Jeff" Ding, his wife Helen Chui and their daughters Xing and Alicewere found murdered at their home in Wootton at 6:00 pm on Sunday, 1 May 2011.  They were thought to have been murdered two days earlier between about 3:00 pm and 4:00 pm on Friday, 29 April 2011the day of the Royal Wedding of Prince William and Kate Middleton which was an additional Public Holiday in the United Kingdom.

La CQ: La CQ is a Mexican/Venezuelan television series created by Pedro Ortíz de Pinedo (who also made "Una familia de diez", directed by Sergio Adrián Sánchez "El Venado", and acted by his father Jorge Ortiz de Pinedo).  Recorded at RCTV Studios in Caracas, it is a co-production between Televisa and Cartoon Network Latin America, making it also the first local original live-action series.  The show achieved high audiences, and its original broadcasting time was 11:00 AM, 4:00 PM and 6:00 PM; currently is broadcast Monday through Friday on Cartoon Network in Latin America, and on Canal 5 in Mexico at 5:30 PM.

Sugbuanon Na Ni: Sugbuanon Na Ni is a Philippine weekly informative radio program hosted by Ahmed Cuizon aired on DYAB in Central Visayas.  The show covers Cebuano/Sugbuanon culture.  It is aired from 4:00 PM to 6:00 PM every Sunday.

Faceboy: Francis "Faceboy" Hall is an actor, producer, and activist working in the New York City arts community.  Hall, the younger brother of poet and King Missile frontman, John S. Hall, is one of the founding members of the Art Stars.  Hall has appeared in numerous stage productions and several films, including Robert Downey Sr.'s "Too Much Sun" and the television series 'Electra Elf'.  In addition, Hall was a founding member of the Dance Liberation Front where he has worked to overturn New York City's "no dancing" cabaret laws.  A poet and performer himself, Faceboy is best known as the host of the weekly Faceboyz Open Mic, which is now considered to be the longest continually running open mic in New York.  He hosted 'Faceboyz Folliez', a monthly show that took place at the Bowery Poetry Club.

Good Life Cafe: The Good Life Cafe was a health food market and cafe in Los Angeles, California, known for its open mic nights that helped the 1990s Los Angeles alternative hip hop movement flourish.  In 2008, director Ava DuVernay, who had performed at the cafe with the Figures of Speech hip hop group, released a documentary about the cafe, "This Is The Life".  The film featured a number of hip hop artists discussing the importance of the Good Life Cafe to themselves and the hip hop scene.  The Cafe was open from 1989 to 1999.

El Paso BOTA Port of Entry: The El Paso BOTA Port of Entry, located at the Bridge Of The Americas (BOTA), connecting Mexican Federal Highway 45 to the south and Interstate 110 to the north, is El Paso's highest volume border crossing, carrying more than half the vehicles (trucks and passenger cars) entering El Paso, Texas from Mexico.  This is due in large part to the fact that BOTA is the only bridge in between Mexico and Texas that does not charge a toll.  It is a "Class A" service port with a full range of cargo processing functions, and it is open for passenger vehicle traffic 24/7.  It is open for commercial truck inspections 6:00 AM–6:00 PM Weekdays, 6:00 AM–2:00 PM Saturdays.

Demigodz: Demigodz are a hip hop collective founded by Connecticut rappers Open Mic and Reflex.  The group was originally named "The Nobility" but Open Mic renamed the group "The Demigodz" with inspiration from one of his own verses.  The group has changed several times through the years.  As of 2012, the group consists of; Apathy, Celph Titled, Ryu, Esoteric, Motive, & Blacastan.

Hip Hop Shop: The Hip Hop Shop was a clothing store opened in 1993 by fashion designer Maurice Malone that was more well known for its open mic contests than its clothing.  It quickly evolved into one of the main destinations for rap competitions in the Detroit hip hop scene.  The spot, located on 15736 W. Seven Mile Road, had open mic contests that were managed and hosted by rapper Proof on Saturdays from 4:00 - 6:00 P.M. Its rap battles inspired the similar scenes depicted in the movie "8 Mile", starring Eminem.

Proof (rapper): DeShaun Dupree Holton (October 2, 1973 – April 11, 2006), better known by his stage name Proof, was an American rapper and actor from Detroit, Michigan.  During his career, he was a member of the groups 5 Elementz, Funky Cowboys, Promatic, Goon Sqwad and most notably, D12.  He was a close childhood friend of rapper Eminem, who lived on the same block, and was often a hype man at his concerts.  In 2006, Proof was shot and killed during an altercation at the CCC nightclub in Detroit.

Greg James (radio show): Greg James is a British weekday radio show hosted on BBC Radio 1 at drivetime, starring Greg James as the main presenter.  It is broadcast Monday to Thursday from 4:00pm until 7:00pm, including a 15-minute break for Newsbeat at 5:45pm.  The main focus of the show is music and entertainment in the form of features and celebrity interviews.  On Fridays, "The Official Chart with Greg James" airs between 4:00pm and 5:45pm and "BBC Radio 1's Dance Anthems with Greg James" airs from 6:00pm to 7:00pm.  The show is award-winning, achieving a Sony Radio Academy Award in 2014 for 'Best Entertainment Programme' and an ARIA in 2016 for 'Best Entertainment Production'.

Question: On Sturdays from 4:00-6:00pm, the Hip Hop Shop had open mic contests hosted by a rapper killed during an altercation at what nightclub?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nightclub_name": {
      "type": "string",
      "description": "The name of the nightclub where the rapper was killed."
    },
    "rapper_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The stage name of the rapper."
        },
        "death_year": {
          "type": "integer",
          "description": "The year the rapper was killed."
        }
      },
      "required": [
        "name",
        "death_year"
      ],
      "additionalProperties": false
    },
    "event_hosted": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of event hosted by the rapper."
        },
        "location": {
          "type": "string",
          "description": "The name of the venue where the event was hosted."
        },
        "day_of_week": {
          "type": "string",
          "description": "The day of the week the event took place."
        },
        "start_time": {
          "type": "string",
          "description": "The start time of the event."
        },
        "end_time": {
          "type": "string",
          "description": "The end time of the event."
        }
      },
      "required": [
        "type",
        "location",
        "day_of_week",
        "start_time",
        "end_time"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "nightclub_name",
    "rapper_details",
    "event_hosted"
  ],
  "additionalProperties": false
}
