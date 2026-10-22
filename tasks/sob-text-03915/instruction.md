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
Conflict theories: Conflict theories are perspectives in sociology and social psychology that emphasize a materialist interpretation of history, dialectical method of analysis, a critical stance toward existing social arrangements, and political program of revolution or, at least, reform.  Conflict theories draw attention to power differentials, such as class conflict, and generally contrast historically dominant ideologies.  It is therefore a macro level analysis of society.  Karl Marx is the father of the social conflict theory, which is a component of the four paradigms of sociology.  Certain conflict theories set out to highlight the ideological aspects inherent in traditional thought.  While many of these perspectives hold parallels, conflict theory "does not" refer to a unified school of thought, and should not be confused with, for instance, peace and conflict studies, or any other specific theory of social conflict.

Marxist bibliography: Marxism is a method of socioeconomic analysis that analyzes class relations and societal conflict, that uses a materialist interpretation of historical development, and a dialectical view of social transformation.  Marxist methodology uses economic and sociopolitical inquiry and applies that to the critique and analysis of the development of capitalism and the role of class struggle in systemic economic change.

Marxism: Marxism is a form of socioeconomic analysis that explores class relations and societal conflict using a materialist interpretation of historical development and a dialectical view of social transformation – it originates from the mid-to-late 19th century works of German philosophers Karl Marx and Friedrich Engels.

Student movements in Korea: The first Korean student movement begun in 1919, when students took part in the Sam-il Movement of 1 March to call for the end of Japanese colonization.  The student movement has since then played a major part in several big political changes in Korea.  Before liberation of Korea from Japanese rule in 1945, the main focus of the student movement was opposing this rule and demanding Korea's independence.  After 1945, the student movement was mainly concerned with righting the wrongs in Korean government.  Students rose for instance against the South Korea's government of Syngman Rhee after the rigged elections in March 1960.  1980 marked a turning point in the South Korean student movement.  After the Gwangju massacre in May 1980, the student movement got a clear vision, partly based on Marxism, and had a pivotal role in the democratization of South Korean society.  Student activism is still common on the 21st century South Korean political scene.

Capital, Volume I: Capital.  Volume I: The Process of Production of Capital (German: "Das Kapital.  Erster Band.  Buch I: Der Produktionsprocess des Kapitals" ) is an 1867 economics book by German philosopher Karl Marx.  In this, the only part of Marx's multi-volume "" to be published during his lifetime, Marx critiques capitalism chiefly from the standpoint of its production processes.  After Marx's death, Friedrich Engels compiled and expanded his friend's notes into volumes "II" (1885) and "III" (1894).

Gwangju Student Independence Movement: The Gwangju Student Independence Movement (Hangul: 광주 학생 독립 운동 Hanja:光州學生獨立運動), or Gwangju Student Movement was a Korean independence movement in Gwangju against the 22 August 1910 to 15 August 1945 Japanese rule of Korea.  The Gwangju Student Independence Movement took place in October and November 1929.  It is considered the second-most important Korean independence movement in the period of the Japanese occupation, with the March 1st Movement considered the most important.  The Gwangju Student Independence Movement spread out throughout the Korean Peninsula.

German student movement: The German student movement (also called 68er-Bewegung, movement of 1968, or soixante-huitaires) was a protest movement that took place during the late 1960s in West Germany.  It was largely a reaction against the perceived authoritarianism and hypocrisy of the West German government and other Western governments, and the poor living conditions of students.  A wave of protests—some violent—swept West Germany, fueled by violent over-reaction by the police and encouraged by contemporary protest movements across the world.  Following more than a century of conservatism among German students, the German student movement also marked a significant major shift to the left and radicalization of student activism.

Marxist aesthetics: Marxist aesthetics is a theory of aesthetics based on, or derived from, the theories of Karl Marx.  It involves a dialectical and materialist, or dialectical materialist, approach to the application of Marxism to the cultural sphere, specifically areas related to taste such as art, beauty, etc.  Marxists believe that economic and social conditions, and especially the class relations that derive from them, affect every aspect of an individual's life, from religious beliefs to legal systems to cultural frameworks.  From one classic Marxist point of view, the role of art is not only to represent such conditions truthfully, but also to seek to improve them (social/socialist realism); however, this is a contentious interpretation of the limited but significant writing by Marx and Engels on art and especially on aesthetics.  For instance, Nikolay Chernyshevsky, who greatly influenced the art of the early Soviet Union, followed the secular humanism of Ludwig Feuerbach more than he followed Marx.

Marx's method: Various Marxist authors have focused on Marx's method of analysis and presentation (historical materialist and logically dialectical) as key factors both in understanding the range and incisiveness of Karl Marx's theoretical writing in general and "Das Kapital " in particular.  One of the clearest and most instructive examples of this is his discussion of "the value-form", which acts as a primary guide or key to understanding the logical argument as it develops throughout the volumes of "Das Kapital ".

Swadeshabhimani Ramakrishna Pillai: K. Ramakrishna Pillai (1878–1916) was a nationalist writer, journalist, editor, and political activist.  He edited "Swadeshabhimani" (The Patriot), the newspaper which became a potent weapon against the rule of the British and the erstwhile princely state of Travancore (Kerala, India) and a tool for social transformation.  His criticism of the Diwan of Travancore, P. Rajagopalachari and the Maharajah led to the eventual confiscation of the newspaper.  Ramakrishna Pillai was arrested and exiled from Travancore in 1910.  Vrithantha Pathra Pravarthanam (1912) and Karl Marx (1912) are among his most noted works in Malayalam, Vrithantha Pathra pravarthanam being the first book on journalism in Malayalam and Karl Marx, the first ever biography of Karl Marx in any Indian language.

Question: The first Korean student movement begun in 1919, when students took part in the Sam-il Movement of 1 March to call for the end of Japanese colonization, after the Gwangju massacre in May 1980, the student movement got a clear vision, partly based on which form of socioeconomic analysis that explores class relations and societal conflict using a materialist interpretation of historical development and a dialectical view of social transformation – it originates from the mid-to-late 19th century works of the German philosopher Karl Marx?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "influenced_movement_name": {
      "type": "string",
      "description": "The name of the student movement that was influenced."
    },
    "turning_point_event": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the event that marked a turning point for the movement."
        },
        "year": {
          "type": "integer",
          "description": "The year the turning point event occurred."
        }
      },
      "required": [
        "name",
        "year"
      ],
      "additionalProperties": false
    },
    "influencing_theory": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the socioeconomic analysis that influenced the movement."
        },
        "description_characteristics": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key characteristics describing the socioeconomic analysis."
        },
        "originator": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the primary originator of the theory."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the originator."
            },
            "work_period": {
              "type": "string",
              "description": "The period when the originator's key works were produced."
            }
          },
          "required": [
            "name",
            "nationality",
            "work_period"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "description_characteristics",
        "originator"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "influenced_movement_name",
    "turning_point_event",
    "influencing_theory"
  ],
  "additionalProperties": false
}
