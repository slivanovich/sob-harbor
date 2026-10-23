{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLiberty Weekend: Liberty Weekend was a four-day celebration of the 1984 restoration and the centenary of the Statue of Liberty (\"Liberty Enlightening the World\") in New York City.  It began on July 3 and ended on July 6, 1986.\n\nConservation-restoration of the Statue of Liberty: The conservation-restoration of the Statue of Liberty spanned from 1984 to 1986.  The Statue of Liberty (\"Liberty Enlightening the World\" by Frédéric Auguste Bartholdi) is a colossal monument on Liberty Island in New York Harbor and is a part of the Statue of Liberty National Monument.  Much of the restoration effort was based on unprecedented restorative methods, owing largely to the fact that metallurgical repair work on such a scale had never been attempted before.  Many professional scientists and engineers, government organizations and various consultants were called in to evaluate and deal with the various problems and tasks facing the restoration effort.\n\nMusée de Radio France: The Musée de Radio France was a museum operated by Radio France and located in the Maison de Radio-France, near the Pont de Grenelle in the XVIe arrondissement at 116, avenue du Président Kennedy, Paris, France.  The museum was established in 1966, and contained a remarkable collection of radios and televisions from their origins to the present day, including the 1793 telegraph by Claude Chappe and early crystal radios.  The museum's 2000 objects include prototypes and commercial devices, archival documents, photographs, and manuscripts, replicas of early radio laboratories and studios, and exhibits featuring research by Edouard Branly, Lee de Forest, Heinrich Hertz, Guglielmo Marconi, James Clerk Maxwell, and Alexander Stepanovich Popov.  In 2007, the museum was closed to the public due to the renovation of the Maison de Radio France.\n\nReplicas of the Statue of Liberty: Hundreds of replicas of the Statue of Liberty (\"Liberty Enlightening the World\") have been created worldwide.\n\nPont de Bir-Hakeim: The pont de Bir-Hakeim, formerly the pont de Passy, is a bridge that crosses the Seine River in Paris, France.  It connects the city's 15th and 16th arrondissements, and passes through the île aux Cygnes.\n\nPont de Grenelle: The pont de Grenelle is a bridge in Paris, France, that crosses the Seine river.  It connects the city's 15th and 16th arrondissements, and passes through the Île aux Cygnes.  Constructed of steel, it is a girder bridge.  The current bridge was constructed in 1966, replacing an earlier bridge that had stood since 1873.  The bridge passes behind a replica of the Statue of Liberty.\n\nStatue of Liberty National Monument: The Statue of Liberty National Monument is a United States national monument located in the U.S. states of New Jersey and New York comprising Liberty Island and Ellis Island.  It includes \"Liberty Enlightening the World\", commonly known as the Statue of Liberty, situated on Liberty Island, and the former immigration station at Ellis Island which opened in 1892 and closed in 1954.  The monument is managed by the National Park Service as part of the National Parks of New York Harbor office.\n\nStatue of Liberty: The Statue of Liberty (Liberty Enlightening the World; French: \"La Liberté éclairant le monde\" ) is a colossal neoclassical sculpture on Liberty Island in New York Harbor in New York City, in the United States.  The copper statue, a gift from the people of France to the people of the United States, was designed by French sculptor Frédéric Auguste Bartholdi and built by Gustave Eiffel.  The statue was dedicated on October 28, 1886.\n\nFlame of Liberty: The Flame of Liberty (\"Flamme de la Liberté\") in Paris is a full-sized, gold-leaf-covered replica of the new flame at the upper end of the torch carried in the hand of the Statue of Liberty (\"Liberty Enlightening the World\") at the entrance to the harbor of New York City since 1886.  The monument, which measures approximately 3.5 metres in height, is a sculpture of a flame, executed in gilded copper, supported by a pedestal of gray-and-black marble.  It is located near the northern end of the Pont de l'Alma, on the Place de l'Alma, in the 8th arrondissement of Paris.\n\nStrengthen the Arm of Liberty: Strengthen the Arm of Liberty was the Boy Scouts of America's theme for the organization's fortieth anniversary celebration in 1950.  The campaign was inaugurated in February with a dramatic ceremony held at the base of the Statue of Liberty (\"Liberty Enlightening the World\").  Approximately 200 BSA Statue of Liberty replicas were installed across the United States.\n\nQuestion: The Pont de Grenelle passes behind a replica of what statute sometimes referred to as \"Liberty Enlightening the World\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"statue_original_name\": {\n      \"type\": \"string\",\n      \"description\": \"The primary name of the statue.\"\n    },\n    \"statue_alternative_name\": {\n      \"type\": \"string\",\n      \"description\": \"An alternative name for the statue, as mentioned in the context.\"\n    },\n    \"replica_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_replica_present\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if a replica of the statue is mentioned in the context.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the replica's location relative to a landmark.\"\n        },\n        \"landmark_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the landmark near the replica.\"\n        },\n        \"landmark_city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the landmark is located.\"\n        },\n        \"landmark_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the landmark is located.\"\n        }\n      },\n      \"required\": [\n        \"is_replica_present\",\n        \"location_description\",\n        \"landmark_name\",\n        \"landmark_city\",\n        \"landmark_country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"statue_original_name\",\n    \"statue_alternative_name\",\n    \"replica_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "statue_original_name": {
        "type": "string",
        "description": "The primary name of the statue."
      },
      "statue_alternative_name": {
        "type": "string",
        "description": "An alternative name for the statue, as mentioned in the context."
      },
      "replica_details": {
        "type": "object",
        "properties": {
          "is_replica_present": {
            "type": "boolean",
            "description": "Indicates if a replica of the statue is mentioned in the context."
          },
          "location_description": {
            "type": "string",
            "description": "A description of the replica's location relative to a landmark."
          },
          "landmark_name": {
            "type": "string",
            "description": "The name of the landmark near the replica."
          },
          "landmark_city": {
            "type": "string",
            "description": "The city where the landmark is located."
          },
          "landmark_country": {
            "type": "string",
            "description": "The country where the landmark is located."
          }
        },
        "required": [
          "is_replica_present",
          "location_description",
          "landmark_name",
          "landmark_city",
          "landmark_country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "statue_original_name",
      "statue_alternative_name",
      "replica_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
