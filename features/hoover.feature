Feature: Hoover service testing


  Scenario Outline: Hoover navigates the room and cleans patches of dirt
    Given a room with dimensions "<room_x>" by "<room_y>"
    And a hoover starting at position "<start_x>", "<start_y>"
    And the following patches of dirt: "<dirt_positions>"
    When the hoover moves according to "<instructions>"
    Then the final position of the hoover should be "<final_x>", "<final_y>"
    And the number of cleaned patches should be "<cleaned_patches>"

    @skip
    Examples:
      | room_x | room_y | start_x | start_y | dirt_positions  | instructions      | final_x | final_y | cleaned_patches |
      | 5      | 5      | 1       | 2       | 1,0;2,2;2,3     | NNESEESWNWW       | 1       | 3       | 1               |
      | 10     | 10     | 3       | 4       | 1,1;2,2;2,4;4,4 | NESWWNWNESNENNNNN | 2       | 9       | 4               |
      | 7      | 4      | 0       | 0       | 1,1;3,3         | EENNNNNNWWSSS     | 4       | 1       | 1               |


  Scenario Outline: Invalid parameters handling
    Given a request with wrong parameters "<room_x>" "<room_y>" "<start_x>" "<start_y>" "<dirt_positions>" "<instructions>"
    When I send a request with wrong parameters
    Then the service should return a bad request error

    Examples:
      | room_x | room_y | start_x | start_y | dirt_positions | instructions |
      | 0      | 0      | 0       | 0       | 0,0            | N            |
      | 0      | 0      | -1      | -1      | 0,0            | E            |
      | 0      | 0      | -1      | -1      | 1,1            | S            |
      | 0      | 0      | 1       | -2      | 1,1            | N            |
      | 0      | 0      | 1       | 2       | 0,0            | W            |
      | 0      | 0      | 1       | 2       | 1,1            | N            |
      | -1     | 0      | 1       | 2       | 1,1            | N            |
      | 2      | -3     | 1       | 2       | 1,1            | N            |
      | -4     | -3     | 1       | 2       | 1,1            | N            |
      | 5      | 5      | -4      | -2      | 1,1            | N            |
      | 5      | 5      | 1       | -1      | 1,1            | N            |
      | 5      | 5      | -1      | -6      | 1,1            | N            |
      | 5      | 5      | 5       | 5       | 1,1            | N            |
      | 5      | 5      | 6       | 7       | 1,1            | N            |
      | 5      | 5      | 2       | 3       | 8,6            | N            |


  Scenario Outline: Missing payload information
    Given a request with missing payload information "<room_x>" "<room_y>" "<start_x>" "<start_y>" "<instructions>"
    When I send a request with missing payload information
    Then the service should return a missing input error

    Examples:
      | room_x | room_y | start_x | start_y | instructions      |
      | 5      | 5      | 1       | 2       | NNESEESWNWW       |
      | 10     | 10     | 3       | 4       | NESWWNWNESNENNNNN |
      | 7      | 4      | 0       | 0       | EENNNNNNWWSSS     |


  Scenario Outline: Hoover does not move if driving into a wall
    Given a room with dimensions "<room_x>" by "<room_y>"
    And a hoover starting at position "<start_x>", "<start_y>"
    And the following patches of dirt: "<dirt_positions>"
    When the hoover moves according to "<instructions>"
    Then the final position of the hoover should be "<final_x>", "<final_y>"
    And the number of cleaned patches should be "<cleaned_patches>"

    @skip
    Examples:
      | room_x | room_y | start_x | start_y | dirt_positions | instructions | final_x | final_y | cleaned_patches |
      | 5      | 5      | 0       | 0       | 1,0;2,2;2,3    | S            | 0       | 0       | 0               |
      | 5      | 5      | 0       | 0       | 1,0;2,2;2,3    | WW           | 0       | 0       | 0               |
      | 5      | 5      | 4       | 4       | 1,0;2,2;2,3    | NN           | 4       | 4       | 0               |
      | 5      | 5      | 4       | 4       | 1,0;2,2;2,3    | E            | 4       | 4       | 0               |
      | 5      | 5      | 3       | 3       | 1,0;2,2;2,3    | NN           | 3       | 4       | 0               |
      | 5      | 5      | 3       | 3       | 1,0;2,2;2,3    | EE           | 4       | 3       | 0               |

