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
Pointer (user interface): In computing, a pointer or mouse cursor (as part of a personal computer WIMP style of interaction) is a symbol or graphical image on the computer monitor or other display device that echoes movements of the pointing device, commonly a mouse, touchpad, or stylus pen.  It signals the point where actions of the user take place.  It can be used in text-based or graphical user interfaces to select and move other elements.  It is distinct from the cursor, which responds to keyboard input.  The cursor may also be repositioned using the pointer.

Pointing device: A pointing device is an input interface (specifically a human interface device) that allows a user to input spatial (i.e., continuous and multi-dimensional) data to a computer.  CAD systems and graphical user interfaces (GUI) allow the user to control and provide data to the computer using physical gestures by moving a hand-held mouse or similar device across the surface of the physical desktop and activating switches on the mouse.  Movements of the pointing device are echoed on the screen by movements of the pointer (or cursor) and other visual changes.  Common gestures are point and click and drag and drop.

The Mother of All Demos: "The Mother of All Demos" is a name retroactively applied to a landmark computer demonstration, given at the Association for Computing Machinery / Institute of Electrical and Electronics Engineers (ACM/IEEE)—Computer Society's Fall Joint Computer Conference in San Francisco, which was presented by Douglas Engelbart on 9  1968 ( ) (1968--) .

Diana Merry: Diana Merry-Shapiro was a computer programmer for the Learning Research Group of Xerox PARC in the 1970s and 1980s, after having originally been hired as a secretary.  As one of the original developers of the Smalltalk programming language, she wrote the first system for overlapping display windows.  Merry was also one of the co-inventors of the BitBLT ('bit block transfer') routines for Smalltalk, subroutines for performing computer graphics operations quickly which were pivotal in the evolution of user interfaces from text-based computing to graphical user interfaces.

Ivan Sutherland: Ivan Edward Sutherland (born May 16, 1938) is an American computer scientist and Internet pioneer, widely regarded as the "father of computer graphics."  His early work in computer graphics as well as his teaching with David C. Evans in that subject at the University of Utah in the 1970s was pioneering in the field.  Sutherland, Evans, and his students from that era invented several foundations of modern computer graphics.  He received the Turing Award from the Association for Computing Machinery in 1988 for the invention of Sketchpad, an early predecessor to the sort of graphical user interface that has become ubiquitous in personal computers.  He is a member of the National Academy of Engineering, as well as the National Academy of Sciences among many other major awards.  In 2012 he was awarded the Kyoto Prize in Advanced Technology for "pioneering achievements in the development of computer graphics and interactive interfaces".

Visualization software: Visualization software or visualisation software is a range of computer graphics products used to create graphical displays and interfaces for software applications.  These products include libraries of graphical components or graphic objects (e.g., common charts, Gantt charts, diagrams and realistic equipment images) and software editors for building and deploying data displays for applications.  Primarily used in graphical user interfaces, these products support common platforms, including Java, . NET, Flex, and C++, and are used in desktop and web-based applications.  They are used in different industries, including transportation, telecommunications, manufacturing and defense, to display information in formats designed to be easily understood.  These displays are primarily for applications requiring custom, high-performance interfaces that are scalable and industry specific.

Douglas Engelbart: Douglas Carl Engelbart (January 30, 1925 – July 2, 2013) was an American engineer and inventor, and an early computer and Internet pioneer.  He is best known for his work on founding the field of human–computer interaction, particularly while at his Augmentation Research Center Lab in SRI International, which resulted in creation of the computer mouse, and the development of hypertext, networked computers, and precursors to graphical user interfaces.  These were demonstrated at The Mother of All Demos in 1968.  Engelbart's Law, the observation that the intrinsic rate of human performance is exponential, is named after him.

Post-WIMP: In computing, post-WIMP ("windows, icons, menus, pointer") comprises work on user interfaces, mostly graphical user interfaces, which attempt to go beyond the paradigm of windows, icons, menus and a pointing device, i.e. WIMP interfaces.

Box-drawing character: Box-drawing characters, also known as line-drawing characters, are a form of semigraphics widely used in text user interfaces to draw various geometric frames and boxes.  In graphical user interfaces, these characters are much less useful as it is more simple and appropriate to draw lines and rectangles directly with graphical APIs. Box-drawing characters work only with monospaced fonts; however, they are still useful for plaintext comments on websites.

Error message: An error message is information displayed when an unexpected condition occurs, usually on a computer or other device.  On modern operating systems with graphical user interfaces, error messages are often displayed using dialog boxes.  Error messages are used when user intervention is required, to indicate that a desired operation has failed, or to relay important warnings (such as warning a computer user that they are almost out of hard disk space).  Error messages are seen widely throughout computing, and are part of every operating system or computer hardware device.  Proper design of error messages is an important topic in usability and other fields of human–computer interaction.

Question: Douglas Engelbart, presenter of the 'Mother of All demos' computer demonstration at the Association of Computing Machinery is best known for facilitating the development of which computer device in a precursor to graphical user interfaces?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest_name": {
      "type": "string",
      "description": "The name of the person who presented the demonstration."
    },
    "event_name": {
      "type": "string",
      "description": "The name of the computer demonstration."
    },
    "event_host_organization": {
      "type": "string",
      "description": "The organization that hosted the event."
    },
    "developed_device_name": {
      "type": "string",
      "description": "The name of the computer device Douglas Engelbart is best known for facilitating the development of."
    },
    "device_context": {
      "type": "string",
      "description": "The context in which the device was developed, related to user interfaces."
    }
  },
  "required": [
    "person_of_interest_name",
    "event_name",
    "event_host_organization",
    "developed_device_name",
    "device_context"
  ],
  "additionalProperties": false
}
