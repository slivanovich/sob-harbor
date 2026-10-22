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
United States biological weapons program: The United States biological weapons program officially began in spring 1943 on orders from U.S. President Franklin Roosevelt.  Research continued following World War II as the U.S. built up a large stockpile of biological agents and weapons.  Over the course of its 27-year history, the program weaponized and stockpiled the following seven bio-agents (and pursued basic research on many more):

United States chemical weapons program: The United States chemical weapons program began in 1917 during World War I with the creation of the U.S. Army's Gas Service Section and ended 73 years later in 1990 with the country's practical adoption of the Chemical Weapons Convention (signed 1993; entered into force, 1997).  Destruction of stockpiled chemical weapons began in 1985 and is still ongoing.  Alleged use of chemical agents by the U.S. in the Korean (1950–53) and Vietnam (1955-1975) conflicts has never been substantiated and there is no reliable evidence that the country ever used chemical weapons on either battlefield.  The U.S. Army Medical Research Institute of Chemical Defense (USAMRICD), at Aberdeen Proving Ground, Maryland, continues to operate.

Iraqi biological weapons program: Saddam Hussein (1937–2006) initiated an extensive biological weapons (BW) program in Iraq in the early 1980s, in violation of the Biological Weapons Convention (BWC) of 1972.  Details of the BW program—along with a chemical weapons program—surfaced only in the wake of the Gulf War (1990–91) following investigations conducted by the United Nations Special Commission (UNSCOM) which had been charged with the post-war disarmament of Saddam's Iraq.  By the end of the war, program scientists had investigated the BW potential of five bacterial strains, one fungal strain, five types of virus, and four toxins. Of these, three—anthrax, botulinum and aflatoxin—had proceeded to weaponization for deployment.  Because of the UN disarmament program that followed the war, more is known today about the once-secret bioweapons program in Iraq than that of any other nation.

U.S. Army Medical Materiel Center – Korea: The United States Army Medical Materiel Center-Korea (USAMMC-K), a subordinate unit of the U.S. Army Medical Research and Materiel Command at Fort Detrick, Maryland, serves as the Defense Logistics Agency's Theater Lead Agent for Medical Materiel (TLAMM) for Korea.

United States Army Medical Materiel Agency: The United States Army Medical Materiel Agency (USAMMA), a subordinate unit of the U.S. Army Medical Research and Materiel Command (USAMRMC) at Fort Detrick, Maryland, serves as the U.S. Army's executive agent for strategic medical acquisition and logistics programs.

Rihab Taha: Rihab Rashid Taha al-Azawi (born November 12, 1957) is an Iraqi microbiologist, dubbed Dr. Germ by United Nations weapons inspectors, who worked in Saddam Hussein's biological weapons program.  A 1999 report commissioned by the United States Joint Chiefs of Staff and the Defense Intelligence Agency (DIA) named her as one of the world's most dangerous women.  Dr Taha admitted producing germ warfare agents but said they had been destroyed.

List of U.S. biological weapons topics: The United States had an offensive biological weapons program from 1943 until 1969.  Today, the nation is a member of the Biological Weapons Convention and has renounced biological warfare.

U.S. Army Medical Materiel Center – Europe: The United States Army Medical Materiel Center-Europe (USAMMCE), a subordinate unit of the U.S. Army Medical Research and Materiel Command at Fort Detrick, Maryland, serves as the Defense Logistics Agency’s Theater Lead Agent for Medical Materiel (TLAMM) for Europe.

United States biological defense program: The United States biological defense program — in recent years also called the National Biodefense Strategy — began as a small defensive effort that paralleled the country's offensive biological weapons development and production program, active between 1943 and 1969.  Organizationally, the medical defense research effort was pursued first (1956-1969) by the U.S. Army Medical Unit (USAMU) and later, after the discontinuation of the offensive program, by the U.S. Army Medical Research Institute of Infectious Diseases (USAMRIID).  Both of these units were located at Fort Detrick, Maryland, where the U.S. Army Biological Warfare Laboratories were headquartered.  The current mission is multi-agency, not exclusively military, and is purely to develop defensive measures against bio-agents, as opposed to the former bio-weapons development program.

Fort Detrick: Fort Detrick is a United States Army Medical Command installation located in Frederick, Maryland.  Historically, Fort Detrick was the center of the US biological weapons program from 1943 to 1969.  Since the discontinuation of that program, it has hosted most elements of the United States biological defense program.

Question: In which city did the United States Army Medical Materiel Agency host its biological weapons program from 1943 to 1969?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "biological_weapons_program": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The official name of the biological weapons program."
        },
        "start_year": {
          "type": "integer",
          "description": "The year the program officially began."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the offensive program ended."
        }
      },
      "required": [
        "name",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "program_center_location": {
      "type": "object",
      "properties": {
        "installation_name": {
          "type": "string",
          "description": "The name of the military installation that was the center of the program."
        },
        "city": {
          "type": "string",
          "description": "The city where the installation is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the installation is located."
        }
      },
      "required": [
        "installation_name",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "involved_agency": {
      "type": "object",
      "properties": {
        "agency_name": {
          "type": "string",
          "description": "The name of the agency mentioned in the question."
        },
        "agency_location_installation": {
          "type": "string",
          "description": "The military installation where the agency is located."
        }
      },
      "required": [
        "agency_name",
        "agency_location_installation"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "biological_weapons_program",
    "program_center_location",
    "involved_agency"
  ],
  "additionalProperties": false
}
