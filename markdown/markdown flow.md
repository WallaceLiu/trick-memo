# Graph
```
graph TB
    A[ ] --> B[ ]
```
```
graph TD
    A[ ] --> B[ ]
```
```
graph BT
    A[ ] --> B[ ]
```
```
graph RL
    A[ ] --> B[ ]
```
```
graph LR
    A[ ] --> B[ ]
```
# Nodes & shapes
## A node (default)
```
graph LR
    id1
```
# A node with text
```
graph LR
    id1[This is the text in the box]
```
# A node with round edges
```
graph LR
    id1((This is the text in the circle));
```
# A node in an asymetric shape
```
graph LR
    id1>This is the text in the box]
```
# A node (rhombus)
```
graph LR
    id1{This is the text in the box}
```
# Links between nodes
## A link with arrow head
```
graph LR
    A-->B
```
## An open link
```
graph LR
    A --- B
```
# Text on links
```
graph LR
    A-- This is the text --- B
```
```
graph LR
    A---|This is the text|B;
```
## A link with arrow head and text
```
graph LR
    A-->|text|B
```
```
graph LR
    A-- text -->B
```
## Dotted link
```
graph LR
    A -.-> B
```
## Dotted link with text
```
graph LR
    A -. text .-> B
```
## Thick link
```
graph LR
    A ==> B
```
## Thick link with text
```
graph LR
    A == text ==> B
```
# Special characters that break syntax
```
graph LR
    d1["This is the (text) in the box"]
```
## Entity codes to escape characters
```
graph LR
    A["A double quote:#quot;"] -->B["A dec char:#9829;"]
```
# Subgraphs
```
 graph TB
         subgraph one
         a1-->a2
         end
         subgraph two
         b1-->b2
         end
         subgraph three
         c1-->c2
         end
         c1-->a2
```
# Styling and classes

## Styling links

It is possible to style links. For instance you might want to style a link that is going backwards in the flow. As links 
have no ids in the same way as nodes, some other way of deciding what style the links should be attached to is required. 
Instead of ids, the order number of when the link was defined in the graph is used. In the example below the style 
defined in the linkStyle statement will belong to the fourth link in the graph:

linkStyle 3 stroke:#ff3,stroke-width:4px;

## Styling a node

It is possible to apply specific styles such as a thicker border or a different background color to a node. 
%% Example code

graph LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px;
    style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5;

## Classes

More convenient then defining the style every time is to define a class of styles and attach this class to the nodes that 
should have a different look.

a class definition looks like the example below:

 classDef className fill:#f9f,stroke:#333,stroke-width:4px;
1
Attachment of a class to a node is done as per below:

 class nodeId1 className;
1
It is also possible to attach a class to a list of nodes in one statement:

   class nodeId1,nodeId2 className;
1

## Css classes

It is also possible to pre dine classes in css styles that can be applied from the graph definition as in the example 
below:

Example style

Example definition

graph LR;
    A-->B[AAABBB];
    B-->D;
    class A cssClass;
1
2
3
4
Class definitions in the graph defnition is broken in version 0.5.1 
but has been fixed in the master branch of mermaid. This fix will be 
included in 0.5.2

### Default class

If a class is named default it will be assigned to all classes without specific class definitions.

classDef default fill:#f9f,stroke:#333,stroke-width:4px;