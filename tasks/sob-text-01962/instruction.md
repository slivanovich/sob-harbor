{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStudents for Liberty: Students For Liberty (SFL) is an international libertarian non-profit organization (with origins in the United States) whose stated mission is \"to educate, develop, and empower the next generation of leaders of liberty.\"  Formed in 2008 after a meeting at which students shared ideas and experiences about libertarian student groups, SFL has since grown into a full organization with various programs and a network of affiliated student groups.\n\nRock the Vote: Rock the Vote is a non-profit organization, progressive-aligned group in the United States whose stated mission is \"to engage and build the political power of young people.\"\n\nShiv R. Jhawar: Shiv R. Jhawar (born 1948) is an Indian-American author, public speaker and entrepreneur.  He is the author of the book \"Building a Noble World\" and has also published numerous political articles.  He is the founder of \"Noble World Foundation\", a non-profit organization whose stated mission is to promote the inner transformation of individuals through meditation.  He is also outspoken about political reform and is known for his call to the United Nations to reform the UN Charter to allow for regional membership.\n\nNational Center for Science Education: The National Center for Science Education (NCSE) is a not-for-profit membership organization in the United States whose stated mission is to educate the press and the public on the scientific and educational aspects of controversies surrounding the teaching of evolution and climate change, and to provide information and resources to schools, parents, and other citizens working to keep those topics in public school science education.  Based in Oakland, California, it claims 4,500 members that include scientists, teachers, clergy, and citizens of varied religious and political affiliations.  The Center opposes the teaching of religious views in science classes in America's public schools through initiatives such as Project Steve, and has been called the United States' \"leading anti-creationist organization\".  The Center is affiliated with the American Association for the Advancement of Science.\n\nOratorio Society of New York: The Oratorio Society of New York is a not-for-profit membership organization that performs choral music in the oratorio style.  The Society was founded in 1873 by conductor Leopold Damrosch and is the third oldest musical organization in New York City.  The Society had a prominent role in the building of Carnegie Hall.  Throughout its long history, it has premiered many new choral works.\n\nGlenn Branch: Glenn Branch is the Deputy Director of the National Center for Science Education and a prominent critic of creationism and its offshoot, intelligent design.  Branch has a Masters of Arts in Philosophy from the University of California, Los Angeles.\n\nIndependent Book Publishers Association: The Independent Book Publishers Association (IBPA) is a not-for-profit membership organization serving the independent publishing community through advocacy and education.  With nearly 3,000 members, IBPA is the largest publishing trade association in the United States.  IBPA programs and publications include the Benjamin Franklin Awards, Publishing University,\n\nFourth Estate (association): The Fourth Estate is a United States based international, non-partisan, membership organization whose stated mission is to \"contribute to a healthy society by fostering, supporting and incubating a sustainable and vibrant free press.\"\n\nStandardization in Lab Automation: The SiLA consortium is a not-for-profit membership organization formed by software suppliers, system integrators and pharma/biotec corporations.  This consortium for Standardization in Lab Automation (SiLA), develops and introduces new device and data interface standards allowing rapid integration of lab Automation hardware and data management systems.  Highly skilled experts of member companies contribute in SiLA′s technical work groups.  Membership is open for institutions, corporations and individuals active in the life science lab automation industry.  The SiLA consortium provides professional training, support and certification services to suppliers and system integrators implementing SiLA compliant interfaces.\n\nAssistive Technology Industry Association: The Assistive Technology Industry Association (ATIA) is a not-for-profit membership organization of manufacturers, sellers and providers of technology-based assistive devices and/or services, for people with disabilities.  ATIA represents the interests of its members to business, government, education, and the many agencies that serve people with disabilities.  One goal of the ATIA is to \"speak with the common voice\" for Its mission is to serve as the collective voice of the Assistive Technology (AT) industry so that the best products and services are delivered to people with disabilities.\n\nQuestion: What was the position of Glenn Branch in a not-for-profit membership organization in the United States whose stated mission is to educate the press and the public?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization the person is associated with.\"\n    },\n    \"organization_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the organization.\"\n    },\n    \"organization_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the organization is based.\"\n    },\n    \"organization_mission_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of the organization's stated mission relevant to the question.\"\n    },\n    \"person_position\": {\n      \"type\": \"string\",\n      \"description\": \"The position held by the person within the organization.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"organization_name\",\n    \"organization_type\",\n    \"organization_country\",\n    \"organization_mission_summary\",\n    \"person_position\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "organization_name": {
        "type": "string",
        "description": "The name of the organization the person is associated with."
      },
      "organization_type": {
        "type": "string",
        "description": "The type of the organization."
      },
      "organization_country": {
        "type": "string",
        "description": "The country where the organization is based."
      },
      "organization_mission_summary": {
        "type": "string",
        "description": "A summary of the organization's stated mission relevant to the question."
      },
      "person_position": {
        "type": "string",
        "description": "The position held by the person within the organization."
      }
    },
    "required": [
      "person_name",
      "organization_name",
      "organization_type",
      "organization_country",
      "organization_mission_summary",
      "person_position"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
