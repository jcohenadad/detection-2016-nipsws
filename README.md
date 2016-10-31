# Hierarchical Object Detection with Deep Reinforcement Learning

|  ![NIPS 2016 logo][logo-nips] | Paper accepted at [Deep Reinforcement Learning Workshop, NIPS 2016](https://sites.google.com/site/deeprlnips2016/)   |
|:-:|---|

[logo-nips]: http://hci-kdd.org/wordpress/wp-content/uploads/2014/11/Neural-Information-Processing-2016.jpg "NIPS 2016 logo"

| ![Míriam Bellver][bellver-photo]  | ![Xavier Giro-i-Nieto][giro-photo]  | ![Ferran Marqués][marques-photo]  | ![Jordi Torres][torres-photo]  |
|:-:|:-:|:-:|:-:|:-:|
| [Míriam Bellver][bellver-web]  | [Xavier Giro-i-Nieto][giro-web]  |  [Ferran Marques][marques-web] | [Jordi Torres][torres-web]  |


[bellver-web]: https://www.bsc.es/bellver-bueno-miriam
[giro-web]: https://imatge.upc.edu/web/people/xavier-giro
[torres-web]: http://www.jorditorres.org/
[marques-web]:https://imatge.upc.edu/web/people/ferran-marques

[bellver-photo]:  "Míriam Bellver"
[giro-photo]: https://raw.githubusercontent.com/imatge-upc/retrieval-2016-deepvision/master/authors/giro.jpg "Xavier Giro-i-Nieto"
[marques-photo]: https://raw.githubusercontent.com/imatge-upc/retrieval-2016-deepvision/master/authors/marques.jpg "Ferran Marques"
[satoh-photo]:  "Jordi Torres"

A joint collaboration between:

|![logo-bsc] | ![logo-upc] | ![logo-etsetb] | ![logo-gpi]  |
|:-:|:-:|:-:|:-:|
| [Barcelona Supercomputing Center][bsc-web] | [Universitat Politecnica de Catalunya (UPC)][upc-web]   | [UPC ETSETB TelecomBCN][etsetb-web]  | [UPC Image Processing Group][gpi-web] |

[upc-web]: http://www.upc.edu/?set_language=en 
[etsetb-web]: https://www.etsetb.upc.edu/en/ 
[gpi-web]: https://imatge.upc.edu/web/ 
[bsc-web]: http://www.bsc.es

[logo-upc]: https://raw.githubusercontent.com/imatge-upc/retrieval-2016-deepvision/master/logos/upc.jpg "Universitat Politecnica de Catalunya (UPC)"
[logo-etsetb]: https://raw.githubusercontent.com/imatge-upc/retrieval-2016-deepvision/master/logos/etsetb.png "ETSETB TelecomBCN"
[logo-gpi]: https://raw.githubusercontent.com/imatge-upc/retrieval-2016-deepvision/master/logos/gpi.png "UPC Image Processing Group"
[logo-bsc]:  "Barcelona Supercomputing Center"

## Publication
### Abstract

 We present a method for performing hierarchical object detection in images guided by a deep reinforcement learning agent. The key idea is to focus on those parts of the image that contain richer information and zoom on them. We train an intelligent agent that, given an image window, is capable of deciding where to focus the attention among five different predefined region candidates (smaller windows). This procedure is iterated providing a hierarchical image analysis.
 
We compare two different candidate proposal strategies to guide the object search: with and without overlap. Moreover, our work compares two different strategies to extract features from a convolutional neural network for each region proposal: a first one that computes new feature maps for each region proposal, and a second one that computes the feature maps for the whole image to later generate crops for each region proposal. 

Experiments indicate better results for the overlapping candidate proposal strategy and a loss of performance for the cropped image features due to the loss of spatial resolution. We argue that, while this loss seems unavoidable when working with large amounts of object candidates, the much more reduced amount of region proposals generated by our reinforcement learning agent allows considering to extract features for each location without sharing convolutional computation among regions.

### Cite

You can find [our paper] (.pdf) in the [Proceedings of the NIPS Workshop in Reinforcement Learning](.py) at NIPS 2016. 
Our [preprint]() is also available on arXiv. 


````

````


You may also want to refer to our publication with the more human-friendly Chicago style:

````

````

## Code Instructions



### Setup



### Usage

