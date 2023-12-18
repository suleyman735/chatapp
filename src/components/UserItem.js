import { Avatar, ListItem, ListItemAvatar, ListItemText } from '@mui/material'
import React from 'react'
// import ImageIcon from'@mui/icons-material/Image'

export default function UserItem(props) {
  return (
    <ListItem>
        <ListItemAvatar>
            <Avatar>
                jjj
                {/* <ImageIcon ></ImageIcon> */}

            </Avatar>
        </ListItemAvatar>
        <ListItemText primary={props.name} secondary>{props.email}</ListItemText>
    </ListItem>
  )
}
