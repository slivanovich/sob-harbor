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
Soccer Saturday: Gillette Soccer Saturday is a weekly television programme broadcast on Sky Sports in the United Kingdom and Ireland during the football season.  The programme updates viewers on the progress of association football games in the United Kingdom on Saturday afternoons.  The current host is Jeff Stelling.  The programme is sponsored by Gillette.

UK Space Agency: The United Kingdom Space Agency (commonly known as the UK Space Agency or UKSA) is an executive agency of the Government of the United Kingdom, responsible for the United Kingdom's civil space programme.  It was established on 1 April 2010 to replace the British National Space Centre (BNSC) and took over responsibility for government policy and key budgets for space exploration, and represents the United Kingdom in all negotiations on space matters.  It "[brings] together all UK civil space activities under one single management".  It is based at the former BNSC headquarters in Swindon, Wiltshire.

United Kingdom government austerity programme: The United Kingdom government austerity programme is a fiscal policy undertaken in response to the Great Recession.  It is a deficit reduction programme consisting of sustained reductions in public spending and tax rises, intended to reduce the government budget deficit and the welfare state in the United Kingdom.  The National Health Service and education have been "ringfenced" and protected from direct spending cuts.  United Kingdom austerity policies have received pointed criticism from left-wing politicians and economists, and have prompted anti-austerity movements among citizens more generally.

National Lottery (United Kingdom): The National Lottery is the state-franchised national lottery in the United Kingdom.

Syrian Vulnerable Person Resettlement Programme: The Syrian Vulnerable Person Resettlement Programme, sometimes referred to as a Relocation Scheme, is a programme of the United Kingdom government that plans to resettle 20 000 Syrian refugees from refugee camps in Jordan, Lebanon, Iraq, Egypt and Turkey over the period from September 2015 to May 2020.  It was first announced in January 2014 and in September 2015 the expansion to 20,000 refugees was made.  It is run in partnership between the UK Home Office, the Department for International Development, the Department for Communities and Local Government and NGOs such as Refugee Action.  Only 2,659 Syrian refugees were resettled through the programme by the end of June 2016.  The National Audit Office estimated the Programme's cost at £1,112 million.

Who Dares Wins (UK game show): Who Dares Wins is a BBC game show broadcast on BBC One which began on 17 November 2007.  The programme is hosted by Nick Knowles.  It was a BBC National Lottery game show until 21 January 2017.

Abu Bakar bin Abdul Jamal: Admiral (Retired) Tan Sri Dato’ Seri Abu Bakar bin Abdul Jamal was the tenth Chief and the first four-star Admiral of the Royal Malaysian Navy (RMN).  He was born on 13 November 1946 in Johor, Malaysia and received his early education at the Royal Military College in Sungai Besi, Kuala Lumpur.  Admiral Abu Bakar joined the naval service in 1965 and commenced training as a cadet at the Britannia Royal Naval College, United Kingdom.  Admiral Abu Bakar was trained in weapons engineering at HMS "Excellent" School of Weapons Engineering, United Kingdom.  He was also trained in Training Technology by the Royal Australian Navy.  Admiral Abu Bakar is also a graduate of the Royal Naval College, Greenwich, United Kingdom and the Naval Postgraduate School, Monterey, California, where he studied Defence Management.  He went on to enrol in a fellowship programme at the Wolfson College, Cambridge and later studied at the Royal College of Defence Studies, United Kingdom.

Pob's Programme: Pob's Programme is a children's television programme which was broadcast in the United Kingdom on Channel 4 between October 1985 and November 1987.  The programme is presented by a puppet named Pob (played by puppeteer Robin Stevens), who speaks a primitive version of English and who supposedly lives inside the viewer's TV (the casing and red, green and blue electron guns visible behind him).  Music was composed and performed by Mike Stanley.  The opening titles of the show consist of the character breathing on the camera lens (this breathing was often mistaken for spitting, given the loud noise accompanying it and the thick condensation appearing on screen), and tracing his name in the condensation.  Each week on the programme, a celebrity guest visits Pob's garden, and entertains him — though Pob and the guest never appear on screen together.

Astrophysical Virtual Observatory: The Astrophysical Virtual Observatory (AVO) Project conducted a research and demonstration programme on the scientific requirements and technologies necessary to build a VO for European astronomy.  The AVO has been jointly funded by the European Commission (under FP5 - Fifth Framework Programme) with six European organisations participating in a three year Phase-A work programme, valued at 5 million euro.  The partner organisations were the European Southern Observatory (ESO) in Munich, Germany, the European Space Agency (ESA), AstroGrid (funded by PPARC as part of the UK's E-Science programme), the CNRS-supported Centre de Données Astronomiques de Strasbourg (CDS), the University Louis Pasteur in Strasbourg, France, the CNRS-supported TERAPIX astronomical data centre at the Institut d'Astrophysique in Paris, France, and the Jodrell Bank Observatory of the Victoria University of Manchester, United Kingdom.

See Hear: See Hear is a monthly magazine programme for deaf and hard-of-hearing people in the United Kingdom, broadcast on Wednesday mornings at 8:00am.  The programme focuses on the British and the worldwide deaf community and covers a broad range of topics from areas such as education, deaf people's rights, technology and language.  The programme is presented entirely in BSL and is broadcast with voice-over and subtitles in English.  Using these methods allow not only deaf, but also hearing people learning sign language to understand the programme, too.

Question: Who hosts the programme that was state-franchised by the United Kingdom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "program_name": {
      "type": "string",
      "description": "The name of the television programme."
    },
    "program_host": {
      "type": "string",
      "description": "The host of the television programme."
    },
    "franchise_details": {
      "type": "object",
      "properties": {
        "franchise_entity": {
          "type": "string",
          "description": "The entity that state-franchised the program."
        },
        "franchise_status": {
          "type": "string",
          "description": "Describes the program's relationship to the franchise entity."
        }
      },
      "required": [
        "franchise_entity",
        "franchise_status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "program_name",
    "program_host",
    "franchise_details"
  ],
  "additionalProperties": false
}
