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
Pherenikos: Pherenikos (Greek: Φερένικος; Latin: Pherenicus) was an Ancient Greek chestnut racehorse victorious at the Olympic and Pythian Games in the 470s BC.  Pherenikos, whose name means "victory-bearer", was "the most famous racehorse in antiquity".  Owned by Hieron I, tyrant of Syracuse, Pherenikos is celebrated in the victory odes of both Pindar and Bacchylides.

Epinikion: The epinikion or epinicion (plural "epinikia" or "epinicia", Greek ἐπινίκιον , from "epi-", "on," + "nikê", "victory") is a genre of occasional poetry also known in English as a victory ode.  In ancient Greece, the "epinikion" most often took the form of a choral lyric, commissioned for and performed at the celebration of an athletic victory in the Panhellenic Games and sometimes in honor of a victory in war.  Major poets in the genre are Simonides, Bacchylides, and Pindar.

Question: Pherenikos is celebrated in epinikions, what are they?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "term": {
      "type": "string",
      "description": "The Greek term for the genre of poetry."
    },
    "english_name": {
      "type": "string",
      "description": "The common English name for this genre."
    },
    "genre_description": {
      "type": "string",
      "description": "A general description of the genre of poetry."
    },
    "form_in_ancient_greece": {
      "type": "string",
      "description": "The typical form it took in ancient Greece."
    },
    "purpose": {
      "type": "array",
      "description": "The occasions for which epinikia were commissioned and performed.",
      "items": {
        "type": "string"
      }
    },
    "notable_poets": {
      "type": "array",
      "description": "Major poets known for this genre.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "term",
    "english_name",
    "genre_description",
    "form_in_ancient_greece",
    "purpose",
    "notable_poets"
  ],
  "additionalProperties": false
}
