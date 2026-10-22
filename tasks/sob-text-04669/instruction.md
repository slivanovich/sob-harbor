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
Vlastimil Hoferek: Vlastimil Hoferek (born 6 November 1946 in Ostrava) is a Czech former sprint and hurdling athlete who specialised in the 110 metres hurdles and 60 metres hurdles.

Colin Jackson: Colin Ray Jackson, CBE (born 18 February 1967) is a Welsh former sprint and hurdling athlete who specialised in the 110 metres hurdles.  During a career in which he represented Great Britain and Wales, he won an Olympic silver medal, became world champion twice, World indoor champion once, went undefeated at the European Championships for 12 years and was a two-time Commonwealth champion.  His world record of 12.91 seconds for the 110m hurdles stood for over a decade and he remains the 60 metres hurdles world record holder.

Robert Newton (athlete): Robert Alan Newton (born 10 May 1981 in Nottingham, England) is a British hurdling athlete.  As of 2004, he was Britain's number one sprint hurdler.  However, competing for Team GB at the 2004 Summer Olympics in Athens, Newton failed to qualify for the second round of the 110 m hurdles competition.  He was the only openly gay British Olympian that year.

Tony Jarrett: Anthony Alexander Jarrett (born 13 August 1968 in Enfield, London) is a former sprint and hurdling athlete from England.  He was a silver medalist in the 110 metres hurdles at the World Championships in 1993 and 1995, and at the European Championships in 1990, and won the gold medal in the event at the Commonwealth Games in 1998.

Sunday Life (TV series): Sunday Life was a British magazine/discussion television programme broadcast on Sundays on BBC One beginning 20 April 2008.  It was presented by Louise Minchin and Colin Jackson.  The show, which replaced the "Heaven and Earth Show" was intended to focus on "inspiring stories and thought-provoking discussion", with the slogan "Real stories.  Real people.  Real life."  The show was partly intended to fill the public service remit of the BBC's broadcasting licence, as well as its Sunday morning religious quota.  It was dropped from the schedule after one series and its slot in the schedule replaced by The Big Questions.

You're On Sky Sports: You're On Sky Sports was a topical football phone-in discussion television programme on Sky Sports 1 and Sky Sports News Radio.  Originally hosted by Rob Hawthorne then Rob McCaffrey and Gary Newbon, the show was chaired by Jason Cundy.  There will always be one or two panel members, whether former football professionals or others involved with the game in some form.  Regulars include Steve Claridge, Kenny Sansom, Peter Beagrie, Tony Gale and Warren Barton.  The program usually aired at 10pm either the night of a UEFA Champions League match or a Premier League match that is aired on Sky Sports.

The Heaven and Earth Show: The Heaven and Earth Show was a BBC television programme that aired on Sunday mornings from 10am to 11am on BBC One.  The show ran for nine years between 1998 and 2007, looking at spiritual and moral issues.  Over the years it had numerous presenters, and its final presenter was Gloria Hunniford.

Modesto Castillo: Modesto Castillo (born 24 February 1959, in La Romana, Dominican Republic) is a former sprint and hurdling athlete who specialised in the 110 metres hurdles.

The Big Questions: The Big Questions is a faith and ethics television programme usually presented by Nicky Campbell.  It is broadcast live on BBC One between 10:00am and 11:00am on Sunday, replacing "The Heaven and Earth Show" as the BBC's religious discussion programme.

Arto Bryggare: Arto Kalervo Bryggare (born May 26, 1958 in Kouvola) is a Finnish former hurdling athlete.  He was a member of the Parliament of Finland, representing the Social Democratic Party of Finland from 1995 to 1999 and 2003 to 2007.  His personal best time 13.35, made during trials in 1984 Los Angeles Games, is still the record time in Finland and in Nordic countries.  Bryggare made Finnish history by becoming the first Finn to medal in a sprint event shorter than 400 metres.

Question: Who co-presented a discussion television programme on Sunday, which replaced the 'Heaven and Earth Show', with a Welsh former sprint and hurdling athlete?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_show_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the television programme."
        },
        "type": {
          "type": "string",
          "description": "The type of the television programme."
        },
        "replaced_show_name": {
          "type": "string",
          "description": "The name of the show that was replaced by this programme."
        }
      },
      "required": [
        "name",
        "type",
        "replaced_show_name"
      ],
      "additionalProperties": false
    },
    "athlete_presenter": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the athlete who co-presented the show."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the athlete."
        },
        "specialization": {
          "type": "string",
          "description": "The athletic specialization of the presenter."
        }
      },
      "required": [
        "name",
        "nationality",
        "specialization"
      ],
      "additionalProperties": false
    },
    "co_presenter_name": {
      "type": "string",
      "description": "The name of the co-presenter who is not the athlete."
    }
  },
  "required": [
    "tv_show_details",
    "athlete_presenter",
    "co_presenter_name"
  ],
  "additionalProperties": false
}
