{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFinal Cut Studio: Final Cut Studio is a discontinued professional video and audio production suite for Mac OS X from Apple Inc., and a direct competitor to Avid Media Composer in the high-end movie production industry.  It was developed from 2005 to 2011.  Three of its primary applications - Final Cut Pro X, Motion, and Compressor - continue to be developed and are published as separate applications on the Mac App Store.  The legacy boxed version of Final Cut Studio was last made available only through Apple's phone sales, and therefore not online or in Apple Stores.  As of 2017, Fianl Cut Pro 7 is no longer supported and will not run on macOS High Sierra.\n\nFinal Cut Pro: Final Cut Pro is a series of non-linear video editing software programs first developed by Macromedia Inc. and later Apple Inc. The most recent version, Final Cut Pro X 10.3, runs on Intel-based Mac computers powered by OS X El Capitan or later.  The software allows users to log and transfer video onto a hard drive (internal or external), where it can be edited, processed, and output to a wide variety of formats.  The fully rewritten Final Cut Pro X was introduced by Apple in 2011, with the last version of the legacy Final Cut Pro being version 7.0.3.\n\nColor (software): Color was a professional color grading software application produced by Apple Inc. for their Mac OS X operating system.  It is one of the major applications included as part of Apple's Final Cut Studio 3 video production suite.  It was discontinued with the release of Final Cut Pro X, Motion 5, and Compressor 4.\n\nThe Final Cut (song): \"The Final Cut\" is the title track from Pink Floyd's 1983 album \"The Final Cut\".\n\nMichael Dobbs: Michael Dobbs, Baron Dobbs (born 14 November 1948) is a British Conservative politician and best-selling author, most notably for his \"House of Cards\" trilogy.\n\nFinal Cut Pro X: Final Cut Pro X (pronounced \"Final Cut Pro Ten\") is a professional non-linear video editing application published by Apple Inc. as part of their Pro Apps family of software programs.  It was released on June 21, 2011 for sale in the Mac App Store and is the controversial successor to Final Cut Pro (both editors are incompatible and have quite different approaches to editing).\n\nApple Intermediate Codec: The Apple Intermediate Codec is a high-quality 8-bit 4:2:0 video codec used mainly as a less processor-intensive way of working with long-GOP MPEG-2 footage such as HDV.  It is recommended for use with all HD workflows in Final Cut Express, iMovie, and until Final Cut Pro version 5.  The Apple Intermediate Codec abbreviated AIC (by users, Apple Engineers don't use the abbreviation) is designed by Apple Inc. to be an intermediate format in an HDV and AVCHD workflow.  It features high performance and quality, being less processor intensive to work with than other editing formats.  Unlike native MPEG-2 based HDV - and similar to the standard-definition DV codec - the Apple Intermediate Codec does not use temporal compression, enabling every frame to be decoded immediately without decoding other frames.  As a result of this, the Apple Intermediate Codec takes three to four times more space than HDV.\n\nFinal Cut Server: Final Cut Server was Apple's server-based backend for managing Final Cut Studio files (in particular Final Cut Pro) and workflow automation, based on Proximity's artbox package.  Final Cut Server can catalogue any file type and allows for the addition of custom metadata to make those files searchable.  Final Cut Server runs on Apple hardware but the server is accessed through a Java client that runs on PCs and Macs.  In addition to Java, Final Cut Server makes heavy use of the QuickTime framework and requires its installation when used with PC clients.\n\nFinal Cut Express: Final Cut Express is a discontinued video editing software suite created by Apple Inc. It was the consumer version of Final Cut Pro and was designed for advanced editing of digital video as well as high-definition video, which was used by many amateur and professional videographers.  Final Cut Express was considered a step above iMovie in terms of capabilities, but a step underneath Final Cut Pro and its suite of applications.  As of June 21, 2011, Final Cut Express was discontinued, in favor of Final Cut Pro X.\n\nThe Final Cut (TV serial): The Final Cut is a 1995 BBC television serial, the third part of the \"House of Cards\" trilogy.  Directed by Mike Vardy, the serial, based on Michael Dobbs's 1995 novel of the same name, was adapted for television by Andrew Davies.  It details the conclusion of Francis Urquhart's reign as Prime Minister of the United Kingdom.\n\nQuestion: The Final Cut is based on a 1995 novel from an artist that was born in what month?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel.\"\n    },\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author of the novel.\"\n    },\n    \"author_birth_month\": {\n      \"type\": \"string\",\n      \"description\": \"The birth month of the author.\"\n    },\n    \"novel_publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the novel.\"\n    }\n  },\n  \"required\": [\n    \"novel_title\",\n    \"author_name\",\n    \"author_birth_month\",\n    \"novel_publication_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "novel_title": {
        "type": "string",
        "description": "The title of the novel."
      },
      "author_name": {
        "type": "string",
        "description": "The name of the author of the novel."
      },
      "author_birth_month": {
        "type": "string",
        "description": "The birth month of the author."
      },
      "novel_publication_year": {
        "type": "integer",
        "description": "The publication year of the novel."
      }
    },
    "required": [
      "novel_title",
      "author_name",
      "author_birth_month",
      "novel_publication_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
