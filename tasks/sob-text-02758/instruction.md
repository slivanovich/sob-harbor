{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCLHEP: CLHEP (short for \"A Class Library for High Energy Physics\") is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software.  The project is hosted by CERN and currently managed by a collaboration of researchers from CERN and other physics research laboratories and academic institutions.  According to the project's website, CLHEP is in maintenance mode (accepting bug fixes but no further development is expected).\n\nGerard Salton: Gerard A. \"Gerry\" Salton (8 March 1927 in Nuremberg – 28 August 1995), was a Professor of Computer Science at Cornell University.  Salton was perhaps the leading computer scientist working in the field of information retrieval during his time, and \"the father of information retrieval\".  His group at Cornell developed the SMART Information Retrieval System, which he initiated when he was at Harvard.\n\nStanford Physics Information Retrieval System: The Stanford Physics Information Retrieval System (SPIRES) is a database management system developed by Stanford University.  It is used by universities, colleges and research institutions.  The first website in North America was created to allow remote users access to its database.\n\nRocchio algorithm: The Rocchio algorithm is based on a method of relevance feedback found in information retrieval systems which stemmed from the SMART Information Retrieval System which was developed 1960-1964.  Like many other retrieval systems, the Rocchio feedback approach was developed using the Vector Space Model.  The algorithm is based on the assumption that most users have a general conception of which documents should be denoted as relevant or non-relevant.  Therefore, the user's search query is revised to include an arbitrary percentage of relevant and non-relevant documents as a means of increasing the search engine's recall, and possibly the precision as well.  The number of relevant and non-relevant documents allowed to enter a query is dictated by the weights of the a, b, c variables listed below in the Algorithm section.\n\nCarlos E.M. Wagner: Carlos Wagner is a particle physicist.  He specializes in theoretical physics, elementary particles and supersymmetric theories.  He currently works for the High Energy Physics (HEP) division of the Argonne National Laboratory and is also a professor at the Physics Department of the University of Chicago, Enrico Fermi Institute, and the Kavli Institute for Cosmological Physics, University of Chicago.  He also functions as the Head of the ANL High Energy Physics Theory Group.\n\nDigital library: A digital library is a special library with a collection of digital objects that can include text, visual material, audio material, video material, stored as electronic media formats (as opposed to print, or other media. ) , along with means for organizing, storing, and retrieving the files and media contained in the library collection.  Digital libraries can vary immensely in size and scope, and can be maintained by individuals, organizations, or affiliated with established physical library buildings or institutions, or with academic institutions.  The digital content may be stored locally, or accessed remotely via computer networks.  An electronic library is a type of information retrieval system.\n\nINSPIRE-HEP: INSPIRE-HEP is an open access digital library for the field of high energy physics (HEP).  It is the successor of the Stanford Physics Information Retrieval System (SPIRES) database, the main literature database for high energy physics since the 1970s.\n\nCognitive models of information retrieval: Cognitive models of information retrieval rest on the mix of areas such as cognitive science, human-computer interaction, information retrieval, and library science.  They describe the relationship between a person's cognitive model of the information sought and the organization of this information in an information system.  These models attempt to understand how a person is searching for information so that the database and the search of this database can be designed in such a way as to best serve the user.  Information retrieval may incorporate multiple tasks and cognitive problems, particularly because different people may have different methods for attempting to find this information and expect the information to be in different forms.  Cognitive models of information retrieval may be attempts at something as apparently prosaic as improving search results or may be something more complex, such as attempting to create a database which can be queried with natural language search.\n\nSMART Information Retrieval System: The SMART (System for the Mechanical Analysis and Retrieval of Text) Information Retrieval System is an information retrieval system developed at Cornell University in the 1960s.  Many important concepts in information retrieval were developed as part of research on the SMART system, including the vector space model, relevance feedback, and Rocchio classification.\n\nLegal information retrieval: Legal information retrieval is the science of information retrieval applied to legal text, including legislation, case law, and scholarly works.  Accurate legal information retrieval is important to provide access to the law to laymen and legal professionals.  Its importance has increased because of the vast and quickly increasing amount of legal documents available through electronic means.  Legal information retrieval is a part of the growing field of legal informatics.\n\nQuestion: INSPIRE-HEP is an open access digital library for the field of high energy physics (HEP), it is the successor of the Stanford Physics Information Retrieval System (SPIRES), the first website in which continent, that was created to allow remote users access to its database?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"digital_library_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the digital library.\"\n    },\n    \"field_of_study\": {\n      \"type\": \"string\",\n      \"description\": \"The specific field of physics the digital library serves.\"\n    },\n    \"predecessor_system\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"system_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the predecessor information retrieval system.\"\n        },\n        \"system_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the predecessor system (e.g., database management system).\"\n        },\n        \"first_website_context\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the predecessor system's role in the creation of the first website.\"\n        },\n        \"continent_of_first_website\": {\n          \"type\": \"string\",\n          \"description\": \"The continent where the first website associated with the predecessor system was created.\"\n        }\n      },\n      \"required\": [\n        \"system_name\",\n        \"system_type\",\n        \"first_website_context\",\n        \"continent_of_first_website\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"digital_library_name\",\n    \"field_of_study\",\n    \"predecessor_system\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "digital_library_name": {
        "type": "string",
        "description": "The name of the digital library."
      },
      "field_of_study": {
        "type": "string",
        "description": "The specific field of physics the digital library serves."
      },
      "predecessor_system": {
        "type": "object",
        "properties": {
          "system_name": {
            "type": "string",
            "description": "The name of the predecessor information retrieval system."
          },
          "system_type": {
            "type": "string",
            "description": "The type of the predecessor system (e.g., database management system)."
          },
          "first_website_context": {
            "type": "string",
            "description": "Description of the predecessor system's role in the creation of the first website."
          },
          "continent_of_first_website": {
            "type": "string",
            "description": "The continent where the first website associated with the predecessor system was created."
          }
        },
        "required": [
          "system_name",
          "system_type",
          "first_website_context",
          "continent_of_first_website"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "digital_library_name",
      "field_of_study",
      "predecessor_system"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
