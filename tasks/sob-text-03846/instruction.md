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
1990 FIA European Formula Three Cup: The 1990 FIA European Formula Three Cup was the sixth European Formula Three Cup race and the first to be held at the Bugatti Circuit at Le Mans on September 23, 1990.  The race was won by Italian Alessandro Zanardi, driving for RC Motorsport outfit after Michael Schumacher was disqualified from the race and stripped of his race win.  Italian Mirko Savoldi and Frenchman Yvan Muller completed the podium.

FIA European Formula 3 Championship (1975–1984): FIA European Formula 3 Championship was a former European Formula Three racing competition, organised by the FIA.

1986 FIA European Formula Three Cup: The 1986 FIA European Formula Three Cup was the second European Formula Three Cup race and the first to be held at the Autodromo Enzo e Dino Ferrari on October 26, 1986.  The race was won by Italian Stefano Modena, driving for Euroteam outfit, who finished ahead of the previous years winner Alex Caffi and fellow Italian Nicola Larini.

1989 FIA European Formula Three Cup: The 1989 FIA European Formula Three Cup was the fifth European Formula Three Cup race and the first to be held at the Misano World Circuit on October 15, 1989.  The race was won by Italian Gianni Morbidelli, driving for Forti Corse outfit, who finished ahead of fellow Italians Antonio Tamburini and Giovanni Bonanno.

FIA European Formula Three Cup: The FIA European Formula Three Cup was a Formula Three race held annually in Europe from 1985 to 1990 and 1999 to 2004.  The Cup was awarded by the Fédération Internationale de l'Automobile, the world governing body for motorsport, as its main Formula Three title in Europe after the European Formula Three Championship was cancelled in 1984.  A different venue in Europe hosted the Cup each year during its initial run, while the revival in 1999 saw the Cup between the headline event of the Pau Grand Prix.  In 2003 the Formula 3 Euro Series was started, and the event was ended the following year.

1985 European Formula Three Cup: The 1985 European Formula Three Cup was the inaugural European Formula Three Cup race held at the Paul Ricard Circuit on October 27, 1985.  It was won by Italian Alex Caffi in dominant fashion having achieved pole position, fastest lap and the race win, driving for Team Gulf Coloni, who finished ahead of Swede Thomas Danielsson and German Volker Weidler.

Michael Schumacher: Michael Schumacher (] ; born 3 January 1969) is a retired German racing driver who raced in Formula One for Benetton and Ferrari, where he spent the majority of his career, as well as for Mercedes upon his brief return to the sport.  Widely regarded as one of the greatest Formula One drivers, and regarded by some as the greatest of all time, Schumacher is the only driver in history to win seven Formula One World Championships, five of which he won consecutively.  The most successful driver in the history of the sport, Schumacher holds the records for the most World Championship titles (7), the most Grand Prix wins (91), the most fastest laps (77) and the most races won in a single season (13), and according to the official Formula One website, Schumacher is "statistically the greatest driver the sport has ever seen".

1975 FIA European Formula 3 Cup: The 1975 FIA European Formula 3 Cup was the first edition of the FIA European Formula 3 Championship.  The championship consisted of six rounds across the continent.  The season was won by Australian Larry Perkins, with Conny Andersson second and Renzo Zorzi in third.

1979 FIA European Formula 3 Championship: The 1979 FIA European Formula 3 Championship was the fifth edition of the FIA European Formula 3 Championship.  The championship consisted of 12 rounds across the continent.  Future Formula One world champion, Alain Prost took overall victory in five of these rounds which, among other results, made him the drivers champion for 1979, with Michael Bleekemolen finishing in second and Slim Borgudd third.

1987 FIA European Formula Three Cup: The 1987 FIA European Formula Three Cup was the third European Formula Three Cup race and the first to be held at the Silverstone Circuit on October 4, 1987.  The race was won by Briton Steve Kempton, driving for Reynard R&D outfit, who finished ahead of Italian Alberto Apicella and Frenchman Bertrand Gachot.

Question: What year was the man disqualified from the 1990 FIA European Formula Three Cup born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "race_event": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the race event took place."
        },
        "name": {
          "type": "string",
          "description": "The full name of the race event."
        }
      },
      "required": [
        "year",
        "name"
      ],
      "additionalProperties": false
    },
    "disqualified_driver": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the driver who was disqualified."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the disqualified driver."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the disqualified driver."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "answer_birth_year": {
      "type": "integer",
      "description": "The birth year of the disqualified driver, which is the final answer."
    }
  },
  "required": [
    "race_event",
    "disqualified_driver",
    "answer_birth_year"
  ],
  "additionalProperties": false
}
