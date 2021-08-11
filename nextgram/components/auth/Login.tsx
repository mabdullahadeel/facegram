import { useState } from 'react';
import { Flex, Heading, Button, useColorMode, useColorModeValue } from '@chakra-ui/react';
import { AiOutlineGithub } from 'react-icons/ai';
import axios, { AxiosResponse } from 'axios';

interface RequestIntiateAuthRes {
    authorization_url: string
}

function Login() {
    const { toggleColorMode } =  useColorMode();
    const formBackground = useColorModeValue("gray.100", "gray.700");
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const getGitHubAuthURL = () => {
        setIsLoading(true)
        axios.get("http://localhost:8000/api/oauth/o/github/?redirect_uri=http://localhost:3000/login?status=success")
        .then((response) =>{
             const data: RequestIntiateAuthRes = response.data;
             window.location.replace(data.authorization_url);
            })
        .catch(err => console.log(err))
        .finally(() => {
            setIsLoading(false)
        })
    };

    return (
        <Flex
            height="100vh"
            alignItems="center"
            justifyContent="center"
        >
            <Flex
                direction="column"
                alignItems="center"
                background={formBackground}
                p={12}
                rounded={6}
            >
                <Heading
                    mb={6}
                >
                    Log in
                </Heading>
                <Button 
                    colorScheme={useColorModeValue("blackAlpha", "whiteAlpha")}
                    leftIcon={<AiOutlineGithub />}
                    color="white"
                    mb={6}
                    onClick={() => getGitHubAuthURL()}
                    isLoading={isLoading}
                >
                    Log in with GitHub
                </Button>
                <Button
                    width="100%"
                    colorScheme="teal"
                    onClick={toggleColorMode}
                    variant="outline"
                >
                    Toggle Theme
                </Button>
            </Flex>
        </Flex>
    )
}

export default Login;
