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
Spacistor: The spacistor was a type of transistor developed in the 1950s as an improvement over the point-contact transistor and the later alloy junction transistor.  It offered much higher speed than earlier transistors.  It became obsolete in the early 1960s with the development of the diffusion transistor.

Point-contact transistor: A point-contact transistor was the first type of solid-state electronic transistor ever constructed.  It was developed by research scientists John Bardeen, William Shockley, and Walter Brattain at Bell Laboratories in December, 1947.  They worked in a group led by physicist William Shockley.  The group had been working together on experiments and theories of electric field effects in solid state materials, with the aim of replacing vacuum tubes with a smaller, less power-consuming device.

Grown-junction transistor: The grown-junction transistor was the first type of bipolar "junction" transistor made.  It was invented by William Shockley at Bell Labs on June 23, 1948 (patent filed June 26, 1948), six months after the first bipolar point-contact transistor.  The first germanium prototypes were made in 1949.  Bell Labs announced Shockley’s grown-junction transistor on July 4, 1951.

Hot-carrier injection: Hot carrier injection (HCI) is a phenomenon in solid-state electronic devices where an electron or a “hole” gains sufficient kinetic energy to overcome a potential barrier necessary to break an interface state.  The term "hot" refers to the effective temperature used to model carrier density, not to the overall temperature of the device.  Since the charge carriers can become trapped in the gate dielectric of a MOS transistor, the switching characteristics of the transistor can be permanently changed.  Hot-carrier injection is one of the mechanisms that adversely affects the reliability of semiconductors of solid-state devices.

Walter Houser Brattain: Walter Houser Brattain ( ; February 10, 1902 – October 13, 1987) was an American physicist at Bell Labs who, along with fellow scientists John Bardeen and William Shockley, invented the point-contact transistor in December 1947.  They shared the 1956 Nobel Prize in Physics for their invention.  Brattain devoted much of his life to research on surface states.

Jewell James Ebers: Jewell James Ebers (November 25, 1921 – March 1959) was an American electrical engineer who is remembered for the mathematical model of the bipolar junction transistor that he published with John L. Moll in 1954.  The Ebers-Moll model of the transistor views the transistor as a pair of diodes, and the model is a fusion of the models of these diodes.

John N. Shive: John Northrup Shive (February 22, 1913 – June 1, 1984) was an American physicist and inventor.  He made notable contributions in electronic engineering and solid-state physics during the early days of transistor development at Bell Laboratories.  In particular, he produced experimental evidence that holes could diffuse through bulk germanium, and not just along the surface as previously thought.  This paved the way from Bardeen and Brattain's point contact transistor to Shockley's more-robust junction transistor.  Shive is best known for inventing the phototransistor in 1948 (a device that combines the sensitivity to light of a photodiode and the current gain of a transistor), and for the Shive wave machine in 1959 (an educational apparatus used to illustrate wave motion).

BC548: The BC548 is a general-purpose NPN bipolar junction transistor commonly used in European and American electronic equipment.  It is notably often the first type of bipolar transistor hobbyists encounter, and is often featured in designs in hobby electronics magazines where a general-purpose transistor is required.  The BC548 is low in cost and widely available.

Surface-barrier transistor: The surface-barrier transistor is a type of transistor developed by Philco in 1953 as an improvement to the alloy-junction transistor and the earlier point-contact transistor.  Like the modern Schottky transistor, it offered much higher speed than earlier transistors and used metal–semiconductor junctions (instead of semiconductor–semiconductor junctions), but unlike the schottky transistor, both junctions were metal–semiconductor junctions.

John Bardeen: John Bardeen ( ; May 23, 1908 – January 30, 1991) was an American physicist and electrical engineer, the only person to have won the Nobel Prize in Physics twice: first in 1956 with William Shockley and Walter Brattain for the invention of the transistor; and again in 1972 with Leon N Cooper and John Robert Schrieffer for a fundamental theory of conventional superconductivity known as the BCS theory.

Question: A point-contact transistor was the first type of solid-state electronic transistor ever constructed, it was developed by which American physicist, electrical engineer, and research scientist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "transistor_name": {
      "type": "string",
      "description": "The name of the transistor type."
    },
    "development_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the transistor was developed."
        },
        "organization": {
          "type": "string",
          "description": "The organization where the transistor was developed."
        }
      },
      "required": [
        "year",
        "organization"
      ],
      "additionalProperties": false
    },
    "developers": {
      "type": "array",
      "description": "A list of individuals involved in the development of the transistor.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the developer."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the developer, if specified."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions or roles of the developer."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "primary_developer_matching_criteria": {
      "type": "object",
      "description": "The specific developer identified in the question who matches all specified criteria.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the developer."
        },
        "matched_criteria": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The specific qualifications from the question that this developer matches."
        }
      },
      "required": [
        "name",
        "matched_criteria"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "transistor_name",
    "development_details",
    "developers",
    "primary_developer_matching_criteria"
  ],
  "additionalProperties": false
}
