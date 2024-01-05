# Unity JV Language Support

Welcome to the Unity JV language extension for Visual Studio Code! This extension provides support for programming in a new language inspired by Python and Lua, designed to streamline and simplify the process of coding for the Unity game engine.

## Features

- **Syntax Highlighting:** Enjoy syntax highlighting tailored for the Unity JV language to make your code visually appealing and easy to read.
- **Code Rewriting:** The interpreter translates Unity JV code into C# compatible with the Unity engine, enhancing the development workflow.
- **Faster Development:** Write code more quickly and intuitively, leveraging the simplicity of the Unity JV language.

## Getting Started

1. Install the extension from the Visual Studio Code Marketplace.
2. Open a file with the extension `.jv` to start using the Unity JV language features.
3. Experience faster and more efficient development within the Unity environment.

## Usage

The Unity JV language aims to make game development in Unity more accessible and efficient. Write code in Unity JV and let the extension handle the translation to C#.

```jv
// Unity JV Example
func Start():
    print("Hello Unity JV!")

// Translated C# Code
using UnityEngine;

public class YourScript : MonoBehaviour
{
    void Start()
    {
        Debug.Log("Hello Unity JV!");
    }
}
